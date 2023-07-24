def is_power_of_two(n):
    return (n & (n - 1) == 0) and n != 0


def gcd(a, b):
    while b:
        a, b = b, a % b

    return a


def results_in_infinite_loop(banana_count_a, banana_count_b):
    numerator = banana_count_a + banana_count_b
    denominator = gcd(banana_count_a, banana_count_b)
    result = numerator // denominator

    return not (is_power_of_two(result))


def create_wrestling_tournament(banana_list):
    tournament_graph = {i: [] for i in range(len(banana_list))}

    for i in range(len(banana_list)):
        for j in range(i, len(banana_list)):
            if i != j and results_in_infinite_loop(banana_list[i], banana_list[j]):
                tournament_graph[i].append(j)
                tournament_graph[j].append(i)

    return tournament_graph


def graph_comparator(graph):
    return lambda x: len(graph[x])


def distract_the_trainers(graph):
    distracted_trainers = 0
    remaining_nodes = len(graph)

    while len(graph) > 1 and remaining_nodes >= 1:
        min_length_path = min(graph, key=graph_comparator(graph))

        if (len(graph[min_length_path])) < 1:
            del graph[min_length_path]
        else:
            matched_pair = [len(graph[graph[min_length_path][0]]) + 1, 1]

            for node in graph[min_length_path]:
                if len(graph[node]) < matched_pair[0]:
                    matched_pair = [len(graph[node]), node]

                for i in range(len(graph[node])):
                    if graph[node][i] == min_length_path:
                        del graph[node][i]
                        break

            for node in graph[matched_pair[1]]:
                for i in range(len(graph[node])):
                    if graph[node][i] == matched_pair[1]:
                        del graph[node][i]
                        break

            del graph[min_length_path]
            del graph[matched_pair[1]]
            distracted_trainers += 2

        if len(graph) > 1:
            remaining_nodes = len(graph)

    return distracted_trainers


def solution(banana_list):
    num_trainers = len(banana_list)

    if num_trainers < 1 or num_trainers > 100:
        return None

    if num_trainers == 2 and banana_list[0] == banana_list[1]:
        return num_trainers

    max_bananas_per_trainer_at_start = pow(2, 30) - 1

    for banana_count in banana_list:
        if banana_count > max_bananas_per_trainer_at_start:
            return None

    tournament_graph = create_wrestling_tournament(banana_list)
    distracted_trainers = distract_the_trainers(tournament_graph)
    remaining_trainers = len(banana_list) - distracted_trainers

    return remaining_trainers

if __name__ == '__main__':
    print(solution([1,1]))