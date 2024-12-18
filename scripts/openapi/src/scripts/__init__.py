from .functions import set_dns


def tailscale_dns():
    set_dns(["10.0.40.4", "1.1.1.1"])


def tailscale_fallback_dns():
    set_dns(["10.0.40.4", "1.1.1.1"])
