//urbanmorph_project_01_07.04.25(Satyam)-first-geospatial-planning-project

import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def load_images(folder_path):
    images = []
    years = sorted(os.listdir(folder_path))
    for year in years:
        year_path = os.path.join(folder_path, year)
        for file in os.listdir(year_path):
            if file.endswith(".jpg") or file.endswith(".png"):
                img_path = os.path.join(year_path, file)
                img = cv2.imread(img_path)
                img = cv2.resize(img, (2560, 1124))
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                images.append((int(year), gray))
    return sorted(images)

def compute_change_map(img1, img2):
    diff = cv2.absdiff(img1, img2)
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    return thresh

if __name__ == "__main__":
    folder_path = "../data/raw_images"
    images = load_images(folder_path)

    change_maps = []
    years = []
    change_values = []

    for i in range(len(images) - 1):
        y1, img1 = images[i]
        y2, img2 = images[i + 1]
        diff_map = compute_change_map(img1, img2)

        out_path = f"../outputs/visualizations/change_map_{y1}_{y2}.png"
        cv2.imwrite(out_path, diff_map)

	# Optional: Save side-by-side comparison for visual verification
        stacked = np.hstack((img1, img2, diff_map))
        side_by_side_path = f"../outputs/visualizations/side_by_side_{y1}_{y2}.png"
        cv2.imwrite(side_by_side_path, stacked)


        change_pixel_count = np.sum(diff_map > 0)
        years.append(y1)
        change_values.append(change_pixel_count)

    # Plotting growth
    plt.plot(years, change_values, marker='o')
    plt.title("Urban Change Over Time")
    plt.xlabel("Year")
    plt.ylabel("Change Pixels")
    plt.grid(True)
    plt.savefig("../outputs/predictions/urban_change_trend.png")
    plt.show()

    # Predict future
    X = np.array(years).reshape(-1, 1)
    y = np.array(change_values)
    model = LinearRegression()
    model.fit(X, y)

    future_years = np.array([[2025], [2030], [2035]])
    predictions = model.predict(future_years)

    print("\n📊 Future Urban Growth Predictions:")
    for year, pred in zip(future_years, predictions):
        print(f"{year[0]}: {int(pred)} changed pixels")
