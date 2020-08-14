import huaweisms.api.common


XML_TEMPLATE = (
    '<?xml version="1.0" encoding="UTF-8"?>'
    '<request>'
    '<dataswitch>{enable}</dataswitch>'
    '</request>'
)


def connect_mobile(ctx: huaweisms.api.common.ApiCtx, proxy=None):
    return switch_mobile_on(ctx, proxy=proxy)


def disconnect_mobile(ctx: huaweisms.api.common.ApiCtx, proxy=None):
    return switch_mobile_off(ctx, proxy=proxy)


def get_mobile_status(ctx: huaweisms.api.common.ApiCtx, proxy=None):
    url = "{}/dialup/mobile-dataswitch".format(ctx.api_base_url)
    result = huaweisms.api.common.get_from_url(url, ctx, proxy=proxy)
    if result and result.get('type') == 'response':
        response = result['response']
        if response and response.get('dataswitch') == '1':
            return 'CONNECTED'
        if response and response.get('dataswitch') == '0':
            return 'DISCONNECTED'
    return 'UNKNOWN'


def switch_mobile_off(ctx: huaweisms.api.common.ApiCtx, proxy=None):
    data = XML_TEMPLATE.format(enable=0)
    headers = {
        '__RequestVerificationToken': ctx.token,
    }
    url = "{}/dialup/mobile-dataswitch".format(ctx.api_base_url)
    return huaweisms.api.common.post_to_url(url, data, ctx, additional_headers=headers, proxy=proxy)


def switch_mobile_on(ctx: huaweisms.api.common.ApiCtx, proxy=None):
    data = XML_TEMPLATE.format(enable=1)
    headers = {
        '__RequestVerificationToken': ctx.token,
    }
    url = "{}/dialup/mobile-dataswitch".format(ctx.api_base_url)
    return huaweisms.api.common.post_to_url(url, data, ctx, additional_headers=headers, proxy=proxy)


def switch_net_mode(ctx: huaweisms.api.common.ApiCtx, net_mode='lte_umts', proxy=None):
    xml_template = (
    '<?xml version="1.0" encoding="UTF-8"?>'
    '<request>'
    '<NetworkMode>{mode}</NetworkMode>'
    '<NetworkBand>3FFFFFFF</NetworkBand>'
    '<LTEBand>7FFFFFFFFFFFFFFF</LTEBand>'
    '</request>'
    )
    if net_mode == 'lte':
        data = xml_template.format(mode='03')
    elif net_mode == 'umts':
        data = xml_template.format(mode='02')
    elif net_mode == 'lte_umts':
        data = xml_template.format(mode='0302')
    else:
        data = xml_template.format(mode='0302')
    headers = {
        '__RequestVerificationToken': ctx.token,
    }
    url = "{}/net/net-mode".format(ctx.api_base_url)
    return huaweisms.api.common.post_to_url(url, data, ctx, additional_headers=headers, proxy=proxy)


def get_net_mode(ctx: huaweisms.api.common.ApiCtx, proxy=None):
    url = "{}/net/net-mode".format(ctx.api_base_url)
    result = huaweisms.api.common.get_from_url(url, ctx, proxy=proxy)
    if result and result.get('type') == 'response':
        response = result['response']
        if response and response.get('NetworkMode') == '0302':
            return 'lte_umts'
        if response and response.get('NetworkMode') == '03':
            return 'lte'
        if response and response.get('NetworkMode') == '02':
            return 'umts'
    return 'UNKNOWN_MODE'
