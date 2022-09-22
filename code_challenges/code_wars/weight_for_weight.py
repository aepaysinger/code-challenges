def weight_for_weight(weights):
    weights = weights.split()
    return weights, " ".join(sorted(weights, key=lambda v: sum([int(n) for n in list(v)])))


if __name__ == "__main__":
    weights = "103 123 4444 99 2000"
    print(weight_for_weight(weights))




# def weight_for_weight(weigths):
#     assigned_weights = assign_new_weight(weights)
#     weight_order = weight_order(weights)
#     new_weights_order = f""
#     for weight in 
   
# def weight_order(weights):
#     assigned_weights = assign_new_weight(weights)
#     weights_order = []
#     while assigned_weights:
#         for weight in assigned_weights:
#             smallest_new = list(assigned_weights.values())[0]
#             smallest_old = list(assigned_weights.keys())[0]
#             if assigned_weights[weight] < smallest_new:
#                 smallest_new = assigned_weights[weight]
#                 smallest_old = weight
#                 weights_order.append(smallest_new)
#         del assigned_weights[smallest_old]
#     return weights_order

# def assign_new_weight(weights):
#     new_weights = {}
#     weights = list(weights.split(" "))
#     for weight in weights:
#         new_weights[weight] = sum([int(number) for number in weight])
#     return new_weights
# if __name__ == "__main__":
#     weights = "103 123 4444 99 2000"
#     print(weight_for_weight(weights))