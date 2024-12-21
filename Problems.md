# LeetCode Problems

## Sumário
1. [#973. K Closest Points to Origin](#973-k-closest-points-to-origin-) 

2. [#493. Reverse Pairs](#493-reverse-pairs-)

3. [#719. Find K-th Smallest Pair Distance](#719-find-k-th-smallest-pair-distance-)

## #973. K Closest Points to Origin 🔶

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Example 1:

![ex1](img/ex_1.jpg)

Input: points = [[1,3],[-2,2]], k = 1

Output: [[-2,2]]

Explanation:

The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2

Output: [[3,3],[-2,4]]

Explanation: 

The answer [[-2,4],[3,3]] would also be accepted.

## Como resolvemos?
Esse problema poderia ser resolvido de forma bem rápida e mais simples utilizando um heap, onde a cabeça do heap, fosse o ponto com a menor distância a origem. Porém queríamos nos desafiar utilizando o algoritmo estudado em sala, de par de pontos mais próximos, a diferença era que um ponto seria fixo.

Entretanto vimos que o algoritmo não seria muito efetivo, pois todos os pontos teria que ser comparado com a origem, então a lógica não funcionaria muito bem. Porém ainda gostaríamos de utilizar a ideia de Dividir e Conquistar, pois é o conteúdo atual, então fizemos uma abordagem utilizando a ideia do quicksort, mas sem a parte de ordenação, apenas utilizando o pivô.

Com isso fizemos um algoritmo recursivo, deixando sempre pontos à esquerda ou a direita do pivô dependendo da distância de cada ponto à origem for menor ou maior do que a do pivô à origem. Mas como queríamos utilizar um conteúdo visto em sala, decidimos mudar a forma de escolha do pivô, colocando o algoritmo da Mediana das Medianas, o que funcionou super bem.

## #493. Reverse Pairs 🔴

Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where:

- 0 <= i < j < nums.length and
- nums[i] > 2 * nums[j].

Example 1:

Input: nums = [1,3,2,3,1]

Output: 2

Explanation: 

The reverse pairs are:

(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1

(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1

Example 2:

Input: nums = [2,4,3,5,1]

Output: 3

Explanation: 

The reverse pairs are:

(1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1

(2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1

(3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1

## Como resolvemos?
A ideia foi de usar o algoritmo visto em sala da contagem de inversões, com uma pequena modificação, que era para a condição para ser um par reverso: nums[i] > 2 * nums[j]. 

Fora isso, o algoritmo é o mesmo visto em sala, de ir dividindo o vetor em dois, de forma recursiva, e ir contando o número de inversões ao merjar dois vetores, por meio da função merge_count().

## #719. Find K-th Smallest Pair Distance 🔴

The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

Example 1:

Input: nums = [1,3,1], k = 1

Output: 0

Explanation: Here are all the pairs:

(1,3) -> 2

(1,1) -> 0

(3,1) -> 2

Then the 1st smallest distance pair is (1,1), and its distance is 0.

Example 2:

Input: nums = [1,1,1], k = 2

Output: 0

Example 3:

Input: nums = [1,6,1], k = 3

Output: 5

## Como resolvemos?

Utiizamos a ideia do Dividir e Conquistar, primeiramente ordenando o vetor dos pontos, para facilitar o cálculo das distâncias máximas e depois de forma recursiva encontramos o número de pares possíveis menor que essa distância. E assim, comparando com o k fornecido.