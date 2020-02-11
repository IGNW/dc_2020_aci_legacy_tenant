
resource "aci_tenant" "tenant" {
  name = "IceStone"
}

resource "aci_vrf" "vrf" {
  tenant_dn = "${aci_tenant.tenant.id}"
  name = "IceStone_VRF"
}

resource "aci_application_profile" "app_profile" {
  tenant_dn  = "${aci_tenant.tenant.id}"
  name       = "web_app"
}
