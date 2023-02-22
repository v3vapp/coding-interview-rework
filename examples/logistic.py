###########################################
# This code was mainly written by ChatGPT for the purpose of learning.
########################################### 

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def eratosthenes_sieve(n):
    """
    エラトステネスの篩による素数判定
    n以下の素数を返す
    """
    if n < 2:
        return []
    
    prime = [True] * (n + 1)
    prime[0], prime[1] = False, False
    
    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
    
    return [i for i in range(n + 1) if prime[i]]

# 1-1000までの素数を取得
primes = eratosthenes_sieve(1000)

# 素数かどうかを表すラベルを作成
labels = [1 if i in primes else 0 for i in range(1, 1001)]

# ロジスティック回帰モデルを作成して学習
model = LogisticRegression()
model.fit([[i] for i in range(1, 1001)], labels)

# 1001-2000までの素数を検証
test_primes = eratosthenes_sieve(2000)[len(primes):]
test_labels = [1 if i in test_primes else 0 for i in range(1001, 2001)]

# 予測を行い、精度を計算
predictions = model.predict([[i] for i in range(1001, 2001)])
accuracy = accuracy_score(test_labels, predictions)

print("Accuracy:", accuracy)
