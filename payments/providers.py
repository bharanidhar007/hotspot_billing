# Placeholder parsers for different mobile money providers
def handle_mpesa_ke(data):
    return {'provider':'safaricom_mpesa','amount':data.get('amount'),'currency':data.get('currency','KES'),
            'transaction_id':data.get('transaction_id'),'phone':data.get('phone'),'hotspot_id':data.get('hotspot_id')}
def handle_mpesa_tz(data):
    return {'provider':'vodacom_mpesa','amount':data.get('amount'),'currency':data.get('currency','TZS'),
            'transaction_id':data.get('transaction_id'),'phone':data.get('phone'),'hotspot_id':data.get('hotspot_id')}
def handle_mtn(data):
    return {'provider':'mtn','amount':data.get('amount'),'currency':data.get('currency','UGX'),
            'transaction_id':data.get('transaction_id'),'phone':data.get('phone'),'hotspot_id':data.get('hotspot_id')}
def handle_airtel(data):
    return {'provider':'airtel','amount':data.get('amount'),'currency':data.get('currency','UGX'),
            'transaction_id':data.get('transaction_id'),'phone':data.get('phone'),'hotspot_id':data.get('hotspot_id')}
def handle_tigo_pesa(data):
    return {'provider':'tigo_pesa','amount':data.get('amount'),'currency':data.get('currency','TZS'),
            'transaction_id':data.get('transaction_id'),'phone':data.get('phone'),'hotspot_id':data.get('hotspot_id')}
