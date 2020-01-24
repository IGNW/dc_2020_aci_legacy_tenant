
resource "aci_tenant" "tenant" {
  name = var.tenant_name
}

resource "aci_vrf" "vrf" {
  tenant_dn = "${aci_tenant.tenant.id}"
  name = var.vrf_name
}

resource "aci_bridge_domain" "bridge_domain" {
  tenant_dn = "${aci_tenant.tenant.id}"
  name = var.bd_name
  relation_fv_rs_ctx = "${aci_vrf.vrf.name}"
}

resource "aci_subnet" "subnet" {
  for_each = toset(var.subnets)
  bridge_domain_dn = "${aci_bridge_domain.bridge_domain.id}"
  ip = each.value
}
