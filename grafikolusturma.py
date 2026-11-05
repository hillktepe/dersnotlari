import matplotlib.pyplot as plt

zaman = [0,1,2,3,4,5,6,7,8,9,10]
parlaklik = [10.0,10.8,10.3,9.5,10.0,10.8,10.3,9.5,10.0,10.8,10.3]

plt.figure(figsize=(8,5))

plt.plot(zaman,parlaklik,marker='o',linestyle='-',label='Yıldızın Parlaklığı')

plt.title("Değişen Yıldızın Parlaklık-Zaman Grafiği")
plt.xlabel("Zaman (gün)")
plt.ylabel("Göreli Parlaklık")

plt.xlim(0,10)
plt.ylim(9,11)

plt.xticks(range(0,11,1))
plt.yticks([9.0,9.5,10.0,10.5,11.0])

plt.grid(True, alpha=0.3)
plt.tick_params(axis='both', direction='in')

plt.legend()

plt.tight_layout()

plt.show()

