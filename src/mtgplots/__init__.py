from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.style as mplstyle


styles_path = Path(__file__).parent / "styles"

# Register all .mplstyle files inside the package
plt.style.core.update_nested_dict(
    plt.style.library,
    plt.style.core.read_style_directory(str(styles_path))
)

# Update the list shown by plt.style.available
plt.style.core.available[:] = sorted(plt.style.library.keys())