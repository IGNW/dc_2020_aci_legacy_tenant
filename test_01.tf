resource "aci_bridge_domain" "bridge_domain_192.168.2_V200" {
  tenant_dn               = "${aci_tenant.tenant.id}"
  name                    = "192.168.2_V200"
  relation_fv_rs_ctx      = "${aci_vrf.vrf.name}"
}

resource "aci_subnet" "subnet_192.168.2_V200" {
  bridge_domain_dn        = "${aci_bridge_domain.bridge_domain.id}"
  ip                      = "192.168.2.1/24"
}

resource "aci_application_epg" "epg_192.168.2_V200" {
  application_profile_dn  = "${aci_application_profile.app_profile.id}"
  name                    = "${aci_bridge_domain.bridge_domain.name}"
  description             = "I was built for the some servers!"
  relation_fv_rs_bd       = "${aci_bridge_domain.bridge_domain.name}"
}
