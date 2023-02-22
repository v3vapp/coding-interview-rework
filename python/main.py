import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt

class PrimeNumberChecker:

    def __init__(self, minimum, maximum, sma_length = 30):

        self.minimum = minimum
        self.maximum = maximum
        self.sma_length = sma_length
    
    #---------------------------

    def is_prime(self):

        if self.minimum <= 1:
            self.minimum = 2

        export_prime_list = []
        for i in range(self.minimum, self.maximum+1):
            for j in range(2, i):
                if i%j == 0:
                    break
            else:
                export_prime_list.append(i)

        return export_prime_list

    #---------------------------

    def is_twin_prime(self):

        prime_list = PrimeNumberChecker.is_prime(self)

        twin_prime_list = []

        for i in range(len(prime_list)-1):

            if prime_list[i+1] - prime_list[i] == 2:

                list_temp = []
                list_temp.append(prime_list[i])
                list_temp.append(prime_list[i+1])

                twin_prime_list.append(list_temp)

        return twin_prime_list
    
    #---------------------------

    def primeNumber_pctChange(self):

        target_range = PrimeNumberChecker(self.minimum, self.maximum)
        prime_list = target_range.is_prime()

        df = pd.DataFrame({"prime_number":prime_list})

        # percentage change between prime number and previous prime number
        df["change"] = df.pct_change()
        df["change_normalize"] = df["change"]*100 

        df[f"sma_{self.sma_length}"] = ta.sma(df['change_normalize'], length=self.sma_length)

        # SD between percentage change and simple moving average
        df["SD"] = (df["change_normalize"] - df[f"sma_{self.sma_length}"]).abs()
        df[f"SD_sma_{self.sma_length}"] = ta.sma(df['SD'], length=self.sma_length)

        if self.sma_length <= 1:
            raise ValueError("The input sma_length value has to be larger than 1.")

        if df[f"SD_sma_{self.sma_length}"].sum() == 0:
            print(df[f"SD_sma_{self.sma_length}"])
            raise ValueError("The input sma_length value is too large.")
            
        df[f"SD_sma_{self.sma_length}"] = df[f"SD_sma_{self.sma_length}"].rolling(self.sma_length).sum()/self.sma_length
        # print(df)

        # ------- Chart ------- #
        plt.figure(facecolor="silver", figsize=(20, 10))
        plt.scatter(df["prime_number"], df["change_normalize"], color="fuchsia", s = 4, label="Percentage Change %")
        plt.plot(df["prime_number"], df[f"sma_{self.sma_length}"], color="blue", label=f"SMA {self.sma_length}")
        plt.plot(df["prime_number"], (df[f"sma_{self.sma_length}"] + df[f"SD_sma_{self.sma_length}"]*0.5), color="red",  label=f"SD +1σ")
        plt.plot(df["prime_number"], (df[f"sma_{self.sma_length}"] - df[f"SD_sma_{self.sma_length}"]*0.5), color="red",  label=f"SD -1σ")

        plt.title('Prime Number Percentage Change Between ' + str(self.minimum) + ' and ' + str(self.maximum))
        plt.ylabel('Percentage Change %')
        plt.xlabel('Prime Number')
        plt.legend()
        plt.grid()
        path = "static/result.png"
        plt.savefig(path)
        plt.close()
        
        return path

# ----------------------------------------------------

if __name__ == "__main__":

    data_set = PrimeNumberChecker(5000, 8000, 30)

    prime_list = data_set.is_prime()
    twin_prime_list = data_set.is_twin_prime()
    data_set.primeNumber_pctChange()

    print(prime_list)
    print()
    print(twin_prime_list)
