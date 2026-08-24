from client import BrandedResaleTradeInValuationCircularOsClient

def main():
    client = BrandedResaleTradeInValuationCircularOsClient()
    res = client.process_brand_trade_in('PATAGONIA_NANO_PUFF', 3, 249.0)
    print('Trade-In: ' + res['trade_in_id'] + ' for ' + res['brand_sku'])
    print('Brand Gift Card: $' + str(res['brand_gift_card_credit_usd']) + ' vs Cash: $' + str(res['cash_payout_usd']))
    print('Brand Resale Portal: ' + res['brand_owned_resale_listing_url'] + ' (Passport Minted: ' + str(res['circular_garment_passport_minted']) + ')')

if __name__ == '__main__':
    main()
