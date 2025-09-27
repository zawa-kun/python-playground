# threading ライブラリ
- 並列処理
- 標準ライブラリ
- I/Oバウンドなタスクを複数走らせたい場合において、有効。

### 注意点
- CPythonはPythonコードで実行できるスレッドは１つに限られる。
- <u>マルチコアマシンの計算能力をよりよく利用させたい場合は`multiprocessing`モジュールや`concurrent.futures.ProcessPoolExecutor`の方が良いらしい。</u>

## 通常のPython挙動
**全ての処理がメインスレッド上で直列に動く。**

⇒途中で重い計算や待機処理があっても、その処理が終わるまで後続の処理は実行されない。


## threading ライブラリの利点
並列処理をする事が可能になる。


## 主な関数
### スレッドの作成　threading.Thread()
```Python
hogehoge1 = threading.Thread(target=関数名, args=渡す引数, kwargs= )
```
引数
- `target` : 並列処理するメソッド、関数名
- `args` : 関数に渡す変数
- `kwards` : `キーワード引数。

> `kwards`を使う利点
> 
> - 可読性の向上
> ```Python
> # 悪い例：何の値かわからない
> args=("田中", 30, "Osaka", True, > 5000)
> 
> # 良い例：引数の意味が明確
> args=("田中",),
> kwargs={"age": 30, "city": > > "Osaka", "debug": True, "timeout": > 5000}
> ```
> - 引数の順序に依存しない
> ```Python
> # kwargsなら順序を気にしなくて良い
> kwargs={"timeout": 5000, "debug": True, "city": "Osaka", "age": 30}
> ```
> 
> - デフォルト引数のスキップが可能
> ```Python
> def process(data, format="json", debug=False, timeout=30):
>    pass
>
> # 必要な引数のみ指定可能
>thread = threading.Thread(
>    target=process,
>    args=("データ",),
>    kwargs={"debug": True}  # formatとtimeoutはデフォルト値を使用
>)
> ```

### スレッド処理の開始と待ち start(), join()
```Python
hogehoge1.start()
hogehoge1.join()
```

`スレッド名.start()` : threadの開始。関数の呼び出しのようなもの。
`スレッド名.join()` : threadの処理を待つ