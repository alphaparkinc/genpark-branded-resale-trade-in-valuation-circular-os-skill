class BrandedResaleTradeInValuationCircularOsClient:
    def process_brand_trade_in(self, brand_sku='ARC_ALPHA_SV_JACKET', garment_age_years=2, original_msrp_usd=799.0):
        giftcard_credit_usd = round(original_msrp_usd * 0.45, 2)
        cash_payout_usd = round(original_msrp_usd * 0.32, 2)
        return {
            'trade_in_id': 'arch_tr_99182',
            'brand_sku': brand_sku,
            'brand_gift_card_credit_usd': giftcard_credit_usd,
            'cash_payout_usd': cash_payout_usd,
            'brand_owned_resale_listing_url': 'https://rewear.brand.com/p/alpha_sv_preloved',
            'customer_lifetime_retention_lift_pct': 24.8,
            'circular_garment_passport_minted': True
        }
