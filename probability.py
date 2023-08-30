from matplotlib import pyplot as plt

plt.text(0.01, 0.9, "Рассчитайте вероятность шарика в рулетке", fontsize=15)
plt.text(0.01, 0.8, "казино на красное поле дважды подряд?", fontsize=15)
plt.text(0.01, 0.7, "Если у нас 36 полей рулетки + зеро = 37.", fontsize=15)
plt.text(0.01, 0.6, "Красных полей 18.", fontsize=15)
form = r"$Pr(A) = \frac{n}{N} = (\frac{18}{37})^2 = (0,4864)^2 =$"
plt.text(0.01, 0.4, form, fontsize=20)
form = r"$ = 0,2365*100 = 23,65$"
plt.text(0.01, 0.2, form, fontsize=20)
plt.text(0.01, 0.1, "Вероятность: 23,65 %", fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()