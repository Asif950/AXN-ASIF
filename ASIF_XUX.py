import platform

arch = platform.machine()
if "aarch64" in arch:
    import mew2_64 as mew2
elif "armv7" in arch:
    import mew2_32 as mew2
else:
    raise SystemError("Unsupported architecture!")

# যদি `main` ফাংশন থাকে, তাহলে রান করো
if hasattr(mew2, "main"):
    print("🔹 Running `main()` function...")
    mew2.main()
else:
    print("❌ `main()` function not found!")
