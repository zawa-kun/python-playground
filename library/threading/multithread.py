import threading
import time

# うどんを茹でる関数
def boil_udon():
    print("  ◆スレッド:", threading.currentThread().getName())

    print('  うどんを茹でます。')
    time.sleep(2)
    print('  うどんが茹であがりました。')

# ツユを作る関数
def make_tuyu():
    print("  ◆スレッド:", threading.currentThread().getName())

    print('  ツユをつくります。')
    time.sleep(3)
    print('  ツユができました。')

def boil_noodle(ingredient):
    print("   ♦めんゆでスレッド:", thread1)

    print("  ",ingredient,"を茹でる")
    time.sleep(3)
    print("  ", ingredient, "が茹で上がりました。")


# メイン
if __name__ == "__main__":
    print("◆スレッド:", threading.currentThread().getName())

    ingredient = "ラーメン"
    print(ingredient, 'を作ります。')

    # スレッドを作る
    # thread1 = threading.Thread(target=boil_udon)
    thread1 = threading.Thread(target=boil_noodle, args=(ingredient,))
    thread2 = threading.Thread(target=make_tuyu)

    # スレッドの処理を開始
    thread1.start()
    thread2.start()

    # スレッドの処理を待つ
    # joinはスレッドの処理を待つ関数
    # ↓下２行をコメントアウトすると、40,41行が実行される
    thread1.join()
    thread2.join()

    print('盛り付けます。')
    print('うどんができました。')