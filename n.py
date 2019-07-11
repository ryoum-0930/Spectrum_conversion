# スペクトル用
import wave
from pylab import *
#グラフプロット、保存
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt

import time

# スペクトルを描画する関数
def spctru_out_put(length):
    bgn = 0
    sheet = 0
    sec = 0
    # スペクトログラムを描画
    pxx, freqs, bins, im = specgram(data, NFFT=N, Fs=wf.getframerate(), noverlap=0, window=hammingWindow)
    # axis([0, length, 0, wf.getframerate() / 2])
        #1秒間隔で描画　0.1秒ズレるはず = まだできてない
    for i in np.arange(0,length,0.1):   #0~length 0.1幅
        start = time.time()
        plt.xlim(bgn,bgn+1)
        # plt.savefig('./pictuer/spectrum_%d_%s.png' %( sheet,sec ))
        plt.axis("off")
        plt.savefig(f'./pictuer/spectrum_{sheet}_{str(sec).zfill(2)}.jpg')

        sec +=1
        #ズレる値が変わる
        bgn += 0.1
        #画像の番号
        if sec % 10 ==0:
            sheet = sheet + 1
            sec =0

if __name__ == "__main__":
    # WAVEファイルから波形データを取得
    wf = wave.open("crossing1.wav", "rb")
    data = wf.readframes(wf.getnframes())
    data = frombuffer(data, dtype="int16")
    length = float(wf.getnframes()) / wf.getframerate()  # 波形長さ（秒）

    # FFTのサンプル数
    N = 10001
    time_spc=[]
    # FFTで用いるハミング窓
    for n in range(10):
        start = time.time()
        hammingWindow = np.hamming(N)
        # xlabel("time [second]")
        # ylabel("frequency [Hz]")
        plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
        # スペクトルの描画

        spctru_out_put(length)
        N-=1000

        time_spc.append(time.time() - start)
        # time measure
        print('処理時間：{0}'.format(time_spc[n]) + '[sec]')
    plt.plot(time_spc)
    plt.show()
# 処理時間：63.021684885025024[sec]  :毎回描画するtime
# |
# 処理時間：4.013522148132324[sec]になった　：png_time
# |
# 処理時間：3.2232491970062256[sec]になった ：jpg_time  <=いまここ
