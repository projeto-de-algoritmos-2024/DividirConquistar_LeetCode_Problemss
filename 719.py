from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # Ordenando o array de forma crescente para que o primeiro ponto esteja mais próximo do seu sucessor
        nums.sort()
        
        # Função para contar quantos pares têm distância <= max_dist
        # max_dist distancia entre o primeiro e o último ponto
        def count_pairs(max_dist: int) -> int:
            n_pares, j = 0, 0 
            for i in range(len(nums)):
                # Incrementa j se a distancia entre j e i for menor que a distancia maxima
                while j < len(nums) and nums[j] - nums[i] <= max_dist:
                    j += 1
                # Contando quantos pares tem distancia menor que a max_dist
                n_pares += j - i - 1
            return n_pares
        
        # Função recursiva para busca binária
        def binary_search(left: int, right: int) -> int:
            # Recursão para caso haja apenas um elemento
            if left >= right:
                return left
            # Calcula a metade 
            mid = (left + right) // 2
            # Se n_pares < k (lado esquerdo)
            if count_pairs(mid) < k:
                # Se sim, busca do lado direito
                return binary_search(mid + 1, right)
            else:
                # Se não, busca do lado esquerdo
                return binary_search(left, mid)
        
        # Iniciamos o algoritmo passando o primeiro ponto e o último, para ser a distância max
        return binary_search(0, nums[-1] - nums[0])


# Casos de Teste

solucao = Solution()

nums1 = [1,3,1], k1 = 1
nums2 = [1,1,1], k2 = 2
nums3 = [1,6,1], k3 = 3

r1 = solucao.smallestDistancePair(nums1, k1)
r2 = solucao.smallestDistancePair(nums2, k2)
r3 = solucao.smallestDistancePair(nums3, k3)

print(f"K-ésima menor distancia em {nums1}: {r1}")
print(f"K-ésima menor distancia em {nums2}: {r2}")
print(f"K-ésima menor distancia em {nums3}: {r3}")