class Solution(object):
    def reversePairs(self, nums):
        # Função que vai merjar os vetores L, para parte esquerda, e R para direita, salvando o número de inversões
        def merge_count(L, R):
            # Ponteiros que vão percorrer ambos os vetores
            i, j = 0, 0  
            # Contador de inversões 
            r = 0  
            # Vetor solução merjado
            S_merjado = [] 

            # Conferindo se é um par reverso (L[i] > 2 * R[j])
            while i < len(L) and j < len(R):
                # Se L[i] > 2 * R[j], então há uma inversão
                if L[i] > 2 * R[j]:  
                    # O número em cima da "setinha", que é o número de elementos do vetor da esquerda.
                    r += len(L) - i  
                     # Avança o ponteiro do lado direito
                    j += 1 
                else:   
                    i += 1  # Caso contrário, apenas avança o ponteiro do lado esquerdo

            # Reinicializa os ponteiros
            i, j = 0, 0  
            # Agora sim o merge, em ordem crescente
            while i < len(L) and j < len(R):
                # Se L[i] é menor ou igual a R[j], coloca L[i] primeiro no vetor merjado, e avança seu ponteiro
                if L[i] <= R[j]:  
                    S_merjado.append(L[i])
                    i += 1 
                # Caso contrário, coloca R[j] no vetor S, e avança seu ponteiro
                else:  
                    S_merjado.append(R[j])
                    j += 1  

            # Quando um dos ponteiros estora, só copia o resto do outro vetor
            S_merjado.extend(L[i:])
            S_merjado.extend(R[j:])

             # Retorna a quantidade de inversões e o vetor merjado
            return r, S_merjado 

        # Função recursiva que divide o vetor e vai contando as inversões pela função merge_count
        def count_r(V):
            # Se o tamanho do vetor é 1 ou 0, não há inversões
            if len(V) <= 1:  
                return 0, V 

            # Calcula a metade do vetor para dividir em 2
            mid = len(V) // 2 

            # Chama a função para o lado Esquerdo
            rL, L = count_r(V[:mid])  
            # Chama a função para o lado Direito
            rR, R = count_r(V[mid:])  

            # Conta as inversões ao merjar o lado esquerdo (L) ciom o direito (R)
            r, S = merge_count(L, R)

            # Retorna a soma das inversões nas duas metades e durante o merge
            return rL + rR + r, S 

        # Chama a função count_r passando o vetor de números dado
        r, S = count_r(nums)

        # Retorna o número total de pares reversos
        return r  

# Casos de testes
solucao = Solution()

nums1 = [1,3,2,3,1]
nums2 = [2,4,3,5,1]

r1 = solucao.reversePairs(nums1)
r2 = solucao.reversePairs(nums2)

print(f"Total de pares invertidos em {nums1}: {r1}")
print(f"Total de pares invertidos em {nums1}: {r2}")

