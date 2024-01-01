import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# 초기값 설정
sun_radius = 0.1
earth_radius = 0.05
moon_radius = 0.02
earth_orbit_radius = 5
moon_orbit_radius = 1.5
earth_rotation_period = 1  # 1 프레임당 1도씩 회전
moon_orbit_period = 27  # 달의 공전 주기

# 초기 각도
theta = np.linspace(0, 2*np.pi, 100)

# 초기 위치
x_sun = 0
y_sun = 0

# 지구와 달의 공전 궤도를 나타내는 원의 초기 위치
x_earth_orbit = earth_orbit_radius * np.cos(theta)
y_earth_orbit = earth_orbit_radius * np.sin(theta)

x_moon_orbit = x_earth_orbit[0] + moon_orbit_radius * np.cos(theta)
y_moon_orbit = y_earth_orbit[0] + moon_orbit_radius * np.sin(theta)

# 그래프 초기화 (figsize 추가)
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-8, 8)
ax.set_ylim(-8, 8)
ax.set_aspect('equal', 'box')

# X축과 Y축을 안보이게 설정
ax.set_xticks([])
ax.set_yticks([])

# 태양 서클 추가
sun = plt.Circle((x_sun, y_sun), sun_radius, color='red', label='Sun')
ax.add_patch(sun)

# 지구와 달의 공전 궤도를 원으로 추가
earth_orbit, = ax.plot(x_earth_orbit, y_earth_orbit, linestyle='--', label='Earth Orbit')
moon_orbit, = ax.plot(x_moon_orbit, y_moon_orbit, linestyle='--', label='Moon Orbit')

# 지구 서클 추가
earth, = ax.plot([], [], 'bo', label='Earth')

# 달 서클 추가
moon, = ax.plot([], [], 'o', color='gray', label='Moon')

# 애니메이션 업데이트 함수
def update(frame):
    global x_earth, y_earth, x_moon, y_moon, x_moon_orbit, y_moon_orbit
    # 지구의 공전 주기에 맞게 업데이트
    earth_frame = frame % 360
    x_earth = earth_orbit_radius * np.cos(2*np.pi*earth_frame/360)
    y_earth = earth_orbit_radius * np.sin(2*np.pi*earth_frame/360)
    earth.set_data(np.array([x_earth]), np.array([y_earth]))
    x_moon_orbit = earth_orbit_radius * np.cos(2*np.pi*earth_frame/360)
    y_moon_orbit = earth_orbit_radius * np.sin(2*np.pi*earth_frame/360)
    moon_orbit.set_data(np.array([x_earth]), np.array([y_earth]))


    # 달의 공전 주기에 맞게 업데이트
    moon_frame = frame * (moon_orbit_period / earth_rotation_period) % 360
    x_moon = x_earth + moon_orbit_radius * np.cos(2*np.pi*moon_frame/360)
    y_moon = y_earth + moon_orbit_radius * np.sin(2*np.pi*moon_frame/360)
    moon.set_data(np.array([x_moon]), np.array([y_moon]))

# 태양, 지구, 달 중앙으로 이동
sun.center = (x_sun, y_sun)
earth.set_data([], [])  # 초기화 추가
moon.set_data([], [])  # 초기화 추가
moon_orbit.set_data([], [])

# 애니메이션 생성
num_frames = 1080  # 최소 공배수로 설정
animation = FuncAnimation(fig, update, frames=num_frames, interval=50)

plt.legend()  # 범례 표시
plt.show()
