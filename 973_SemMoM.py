import math

class Solution(object):
    def kClosest(self, points, k):
        # Função para calcular a distância euclidiana até a origem
        def distancia_ate_origem(point):
            # Coordenadas x, y do ponto
            x, y = point
            # Como é até a origem, suas coordenadas são desconsideradas na conta
            return math.sqrt(x**2 + y**2)

        # Função que coloca menores para esquerda do pivô, e os maiores para direita
        def particionar(points, left, right, pivo_i):
            # Salva posição do pivô até origem
            pivo_distancia = distancia_ate_origem(points[pivo_i])
            # Coloca o pivô lá no final, para n atrapalhar na hora de separar
            points[pivo_i], points[right] = points[right], points[pivo_i]
            # A posição do ponto com distância menor que o pivô
            i = left

            # Fica comparando os valores das distancias, e trocando as posições
            for j in range(left, right):
                if distancia_ate_origem(points[j]) < pivo_distancia:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[right] = points[right], points[i]

            # Retorna a posição do pivô
            return i

        # Função recursiva para selecionar os k pontos mais próximos
        def quickselect(points, left, right, k):
            # Apenas um elemento restante
            if left == right:  
                return points[:k]

            # Escolhe o pivô
            pivo_i = (left + right) // 2  
            
            # Particiona os pontos em relação ao pivô
            pivo_final = particionar(points, left, right, pivo_i)

            # Se o número de pontos à esquerda do pivô for igual a k, encontramos a resposta
            if pivo_final == k:
                return points[:k]
            # Se o k, for menor que a posição do pivô, chamar a função para o lado esquerdo
            elif pivo_final > k:
                return quickselect(points, left, pivo_final - 1, k)
            # E se o k, for maior que a posição do pivô, chamar a função para o lado direito
            else:
                return quickselect(points, pivo_final + 1, right, k)
            
        # Chama a função para encontrar os k pontos mais próximo da origem, indo do primeiro ponto 0, até o último, len(points) - 1
        return quickselect(points, 0, len(points) - 1, k)

# Casos de testes
solucao = Solution()

points1 = [[1,3],[-2,2]]
k1 = 1

points2 = [[3,3],[5,-1],[-2,4]]
k2 = 2

s1 = solucao.kClosest(points1, k1)
s2 = solucao.kClosest(points2, k2)

print(f"k pares mais próximos da origem: {s1}")
print(f"k pares mais próximos da origem: {s2}")