resource "aci_application_profile" "app_profile" {
  tenant_dn  = "${aci_tenant.tenant.id}"
  name       = "web_app"
}

resource "aci_application_epg" "epg" {
  for_each = toset(var.epgs)
  application_profile_dn  = "${aci_application_profile.app_profile.id}"
  name = each.value
  relation_fv_rs_bd = "${aci_bridge_domain.bridge_domain.name}"
}
