resource "aci_tenant" "tenant" {
  name = "Icestone"
}

resource "aci_vrf" "vrf" {
  tenant_dn = "${aci_tenant.tenant.id}"
  name = "Icestone"
}

resource "aci_application_profile" "app_profile" {
  tenant_dn  = "${aci_tenant.tenant.id}"
  name       = "LegacyNetworks"
}