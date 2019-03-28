# coding: utf-8

import numpy as np
from data_reader import DataReader
from similarity import computeDistance
import argparse
import kmedoids
import pickle
import random
from pathlib import Path

def genSimilarityMatrix(data):
	indexes=list(data.keys())[:]
	pickleFilePath = Path('data/simMatrix_K_Mediods.pkl')
	if pickleFilePath.exists():
		# Load Pickle File storing the simMatrix
		with open(pickleFilePath, 'rb') as file:
			simMatrix = pickle.load(file)
		return simMatrix,indexes	

	ClusterCount=len(indexes)
	simMatrix = np.ones((ClusterCount, ClusterCount))
	for cID in range(ClusterCount):
		strA = data[indexes[cID]]
		for _cID in range(cID, ClusterCount):
			strB = data[indexes[_cID]]
			similarity_1 = computeDistance(strA, strB)
			simMatrix[cID, _cID] = similarity_1
			simMatrix[_cID, cID] = similarity_1
			#print("similarity between {} and {} = {}\r".format(cID, _cID, similarity_1), end='', flush=True)
			#sys.stdout.flush()
			#print('')
	print(simMatrix)
	with open(pickleFilePath, 'wb') as file:
		pickle.dump(simMatrix, file)
	return simMatrix,indexes		
def solver():
	parser = argparse.ArgumentParser()
	parser.add_argument("integer",type=int,help="Please give arguments as 'Centroid','Min','Max'")
	args = parser.parse_args()
	clusters = args.integer

	reader = DataReader()
	data = reader.loadData()
	simMatrix,indexes = genSimilarityMatrix(data)
	M,C = kmedoids.kMedoids(simMatrix,clusters)
	fileWriter =open('data/Kmedoids_output_{}.txt'.format(clusters),'w') 
	print('medoids',file = fileWriter)
	i=1
	for point in M:
		print('medoid of cluster ',i,' ',indexes[point],file = fileWriter)
		i=i+1
	print(' ',file = fileWriter)
	print('clustering result:',file = fileWriter)
	i=1
	for label in C:
		for point_idx in C[label]:
			print('Cluster ',i,': ',indexes[point_idx],file = fileWriter)
		i=i+1	

	fileWriter.close()	
	print("Clustering Done!!,No. of new clusters are {}".format(clusters))
	print("New clusters are stored in file-data/Kmedoids_output_{}.txt".format(clusters))

if __name__=='__main__':
	solver()

'''
data = np.array([[1,1], 
				[2,2], 
				[10,10]])
'''
# distance matrix
'''
D = pairwise_distances(data, metric='euclidean')

# split into 2 clusters
M, C = kmedoids.kMedoids(D, 2)

print('medoids:')
for point_idx in M:
	print( data[point_idx] )

print('')
print('clustering result:')
for label in C:
	for point_idx in C[label]:
		print('label {0}:　{1}'.format(label, data[point_idx]))

'''

