import sys
sys.path.append(".")  # একই ফোল্ডার থেকে `.so` লোড করতে

import mew2

if hasattr(mew2, "main"):
    print("🔹 Running `main()` function...")
    mew2.main()
else:
    print("❌ `main()` function not found!")
