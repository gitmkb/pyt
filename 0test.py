from pyspark import SparkContext
sc = SparkContext.getOrCreate()

mov_rev = sc.parallelize([('Endgame', 5), ('Solo', 2), ('The Last Jedi', 4)])
print(mov_rev)

mov_rev_coll = mov_rev.collect()
print(mov_rev_coll)

print(mov_rev_coll[2])
