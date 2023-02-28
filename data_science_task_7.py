def calc_investment_metrics(deals_history, current_deal):
    initial_capital = 1000
    deals_sum = 0
    succeeded_deals_count = 0

    for deal_result in deals_history:
        deals_sum += deal_result
        if deal_result > 0:
            succeeded_deals_count += 1

    deals_sum += current_deal

    if deals_sum > 0:
        print(f"total income = {deals_sum}")
    else:
        print(f"total lesion = {deals_sum}")

    roi = ((deals_sum - initial_capital) / initial_capital) * 100
    success_probability = succeeded_deals_count / len(deals_history) * 100

    print(f"ROI = {roi}%")
    print(f"Success probability = {success_probability}%")


def read_int(message):
    read = False
    i = 0
    while not read:
        try:
            i = int(input(message))
            read = True
        except ValueError:
            print("Invalid format! Integer number expected.")
    return i


deals_history_sample = [-107, -521, -107, -126, 352, -58, 221, 193, -38, 454, -12, -211, 129, 85, 342]
current_deal_sample = read_int(">current deal potential profit = ")
calc_investment_metrics(deals_history_sample, current_deal_sample)
