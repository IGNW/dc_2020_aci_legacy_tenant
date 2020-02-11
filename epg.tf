resource "aci_application_epg" "epg" {
  application_profile_dn  = "${aci_application_profile.app_profile.id}"
  name = "VLAN_100"
  relation_fv_rs_bd = "${aci_bridge_domain.bridge_domain.name}"
}

resource "aci_bridge_domain" "bridge_domain" {
  tenant_dn = "${aci_tenant.tenant.id}"
  name = "VLAN_100"
  relation_fv_rs_ctx = "${aci_vrf.vrf.name}"
}

resource "aci_subnet" "subnet" {
  bridge_domain_dn = "${aci_bridge_domain.bridge_domain.id}"
  ip = "192.168.1.1/24"
}
