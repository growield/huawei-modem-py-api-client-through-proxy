from huaweisms.api.common import (
    post_to_url,
    get_from_url,
    ApiCtx,
)


def information(ctx: ApiCtx, proxy=None) -> dict:
    url = "{}/device/information".format(ctx.api_base_url)
    return get_from_url(url, ctx, proxy=proxy)


def basic_information(ctx: ApiCtx, proxy=None) -> dict:
    url = "{}/device/information".format(ctx.api_base_url)
    return get_from_url(url, ctx, proxy=proxy)


def reboot(ctx: ApiCtx, proxy=None) -> dict:
    """
    Reboots the modem.
    """

    url = '{}/device/control'.format(ctx.api_base_url)
    headers = {
        '__RequestVerificationToken': ctx.token,
    }

    payload = '<?xml version: "1.0" encoding="UTF-8"?><request><Control>1</Control></request>'
    return post_to_url(url, payload, ctx, additional_headers=headers, proxy=proxy)
