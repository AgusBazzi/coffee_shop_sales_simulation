import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Read the data
coffee_shop_sales_data = pd.read_csv(
    "../../data/raw/coffee_shop_sales.csv",
    index_col=0,
    usecols=[
        "transaction_id",
        "store_id",
        "product_category",
        "transaction_qty",
        "Size",
        "Month Name",
    ],
)

# Filter out the rows where the store_id is not 8 and the product_category is not Coffee
store_8_coffee_sales = coffee_shop_sales_data.loc[
    (coffee_shop_sales_data["store_id"] == 8)
    & (coffee_shop_sales_data["product_category"] == "Coffee")
]

# Filter out the rows where the size is not defined
store_8_coffee_sales = store_8_coffee_sales.loc[
    store_8_coffee_sales["Size"] != "Not Defined"
]


# Plot the percentages
def plot_percentages(data, key, title):
    percentages = data[key].value_counts(normalize=True) * 100
    ax = percentages.plot(kind="bar")
    for p in ax.patches:
        ax.annotate(
            f"{p.get_height():.2f}%",
            (p.get_x() + p.get_width() / 2.0, p.get_height()),
            ha="center",
            va="center",
            xytext=(0, -10),
            textcoords="offset points",
        )
    plt.title(title)
    plt.show()
    return percentages


sizePercentages = plot_percentages(store_8_coffee_sales, "Size", "Sizes Percentages")

qtyPercentages = plot_percentages(
    store_8_coffee_sales, "transaction_qty", "Qty Percentages"
)


# Export utilities
def getSizePercentage(size):
    return sizePercentages[size] / 100


def getQtyPercentage(qty):
    return qtyPercentages[qty] / 100
