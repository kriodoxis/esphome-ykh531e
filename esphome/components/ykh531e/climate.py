import esphome.codegen as cg
from esphome.components import climate_ir, select
import esphome.config_validation as cv
from esphome.const import CONF_USE_FAHRENHEIT, CONF_ID

AUTO_LOAD = ["climate_ir", "select"]
CODEOWNERS = ["@kriodoxis"]

ykh531e_ns = cg.esphome_ns.namespace("ykh531e")
YKH531EClimate = ykh531e_ns.class_("YKH531EClimate", climate_ir.ClimateIR)
YKH531ETimerSelect = ykh531e_ns.class_("YKH531ETimerSelect", select.Select, cg.Component)

CONF_TIMER_SELECT = "timer_select"

# ── Timer select sub-schema ───────────────────────────────────────────────────
TIMER_SELECT_SCHEMA = select.select_schema(YKH531ETimerSelect).extend(
    {
        cv.Optional("icon", default="mdi:timer-outline"): cv.icon,
    }
)

CONFIG_SCHEMA = climate_ir.climate_ir_with_receiver_schema(YKH531EClimate).extend(
    {
        cv.Optional(CONF_USE_FAHRENHEIT, default=False): cv.boolean,
        cv.Optional(CONF_TIMER_SELECT): TIMER_SELECT_SCHEMA,
    }
)

async def to_code(config):
    var = await climate_ir.new_climate_ir(config)
    cg.add(var.set_fahrenheit(config[CONF_USE_FAHRENHEIT]))
    if timer_conf := config.get(CONF_TIMER_SELECT):
        options = ["Off"] + [f"{i * 0.5:.1f}h" for i in range(1, 49)]
        timer_sel = cg.new_Pvariable(timer_conf[CONF_ID])
        await select.register_select(timer_sel, timer_conf, options=options)
        await cg.register_component(timer_sel, timer_conf)
        cg.add(timer_sel.set_parent(var))
        cg.add(var.set_timer_select(timer_sel))
