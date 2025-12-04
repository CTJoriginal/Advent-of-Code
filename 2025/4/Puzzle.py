import time
import scipy
import numpy as np
import matplotlib.pyplot as plt

solution = []

# to render gif, use this command:
# ffmpeg -f image2 -framerate 20 -i %d.png out.gif
def animation(fmap, step):    
    fig, ax = plt.subplots()
    ax.imshow(fmap, cmap="gray", aspect="equal")
    ax.set_axis_off()
    fig.set_size_inches(10, 10)
    fig.savefig(f"4/anim/{step}.png", dpi = 200, bbox_inches="tight", pad_inches=0.1, facecolor="#ff005176")
    plt.close(fig)
    
st = time.time()
with open("4/input.txt", "r") as inpt:
    fmap = np.array([[1 if c == "@" else 0 for c in n if c != "\n"] for n in inpt.readlines()])

kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) # This kernel will basically just count how many neighbouring tiles are occupied

while True:
    conv = scipy.signal.convolve2d(fmap, kernel)[1:-1, 1:-1] # by default, convolve2d fills boundary with 0's, [1:-1, 1:-1] just slices out original part
    neighMap = conv * fmap # Reset values of empty tiles to 0

    solution.append(np.sum(fmap[neighMap < 4]))
    fmap[neighMap < 4] = 0 
    
    # animation(fmap, len(solution)) # Uncoment to export animation frames
    
    if solution[-1] == 0: break
    
    
t = time.time() - st

print("\n", "=" * 30, sep="")
print(f"Part 1: {solution[0]} - {solution[0] == 1433}")
print(f"Part 2: {np.sum(solution)} - {np.sum(solution) == 8616}")
print("=" * 30,  sep="")
print(f"t: {t:.4f} \n")

