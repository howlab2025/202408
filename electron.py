import numpy as np
import matplotlib.pyplot as plt

def magnetic_field(x, y, m=1):
    r = np.sqrt(x**2 + y**2)
    return m * np.array([3*x*y/r**5, (3*y**2-r**2)/r**5])

fig, ax = plt.subplots(figsize=(10, 8))

x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)

U, V = magnetic_field(X, Y)

# 자기력선 그리기
ax.streamplot(X, Y, U, V, density=2, color='b', linewidth=1, arrowsize=1.5)

# 자석 표시
ax.add_patch(plt.Rectangle((-0.1, -0.5), 0.2, 1, fc='r'))
ax.text(0, 0.6, 'N', ha='center', va='center', color='w', fontweight='bold')
ax.text(0, -0.6, 'S', ha='center', va='center', color='w', fontweight='bold')

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.set_title('자석 주위의 자기장 시뮬레이션')
ax.set_xlabel('X')
ax.set_ylabel('Y')

plt.show()