# Day 3 — Pandas

## 📌 What I learned

* How `merge` works and why duplicates appear
* Difference between one-to-many and many-to-many joins
* Using `apply` with `axis=1` for row-level logic
* Difference between `apply` and vectorized operations

## ⚠️ Mistakes

* Used wrong column name (`ststus`)
* Confused `==` with assignment
* Tried to use `elif` inside lambda
* Misunderstood how `apply` works with columns vs rows

## 🧠 Key concepts

* `merge` creates all matching combinations
* `axis=0` → column-wise
* `axis=1` → row-wise
* `apply` is slower than vectorized operations

## 💡 Insight

Data must be cleaned (duplicates, structure) before analysis, otherwise results can be misleading.

## ✅ Conclusion

Now I understand how to:

* properly merge datasets
* create features using conditional logic
* perform basic segmentation analysis
