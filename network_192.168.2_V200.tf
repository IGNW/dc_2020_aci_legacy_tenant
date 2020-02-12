resource "aci_bridge_domain" "bridge_domain_192_168_2_V200" {
  tenant_dn               = "${aci_tenant.tenant.id}"
  relation_fv_rs_ctx      = "${aci_vrf.vrf.name}"
  name                    = "192.168.2_V200"
}

resource "aci_subnet" "subnet_192_168_2_V200" {
  bridge_domain_dn        = "${aci_bridge_domain.bridge_domain_192_168_2_V200.id}"
  ip                      = "192.168.2.1/24"
  scope                   = "private"
}

resource "aci_application_epg" "epg_192_168_2_V200" {
  application_profile_dn  = "${aci_application_profile.app_profile.id}"
  name                    = "${aci_bridge_domain.bridge_domain_192_168_2_V200.name}"
  description             = "I was built for the some servers!"
  relation_fv_rs_bd       = "${aci_bridge_domain.bridge_domain_192_168_2_V200.name}"
}
