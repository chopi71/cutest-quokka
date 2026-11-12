"""make.fun cutest-picture-01 entry: copies the picture to the output."""
import os
import shutil
from pathlib import Path

src = Path(__file__).parent / "entry.png"
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
# Copy via a temp file and rename, so the output is never a truncated
# picture if the process dies mid-copy.
tmp = out_dir / "entry.png.tmp"
shutil.copyfile(src, tmp)
tmp.replace(out_dir / "entry.png")
