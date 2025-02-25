document.getElementById('id_WS_current').disabled = true;
document.getElementById('id_BS_current').disabled = true;
document.getElementById('id_S_current').disabled = true;
document.getElementById('id_T_current').disabled = true;
document.getElementById('id_I_current').disabled = true;
document.getElementById('id_Ag_current').disabled = true;
document.getElementById('id_Dex_current').disabled = true;
document.getElementById('id_Int_current').disabled = true;
document.getElementById('id_WP_current').disabled = true;
document.getElementById('id_Fel_current').disabled = true;

document.getElementById('id_art_characteristics').disabled = true;
document.getElementById('id_athletics_characteristics').disabled = true;
document.getElementById('id_bribery_characteristics').disabled = true;
document.getElementById('id_charm_characteristics').disabled = true;
document.getElementById('id_charm_animal_characteristics').disabled = true;
document.getElementById('id_climb_characteristics').disabled = true;
document.getElementById('id_cool_characteristics').disabled = true;
document.getElementById('id_consume_alcohol_characteristics').disabled = true;
document.getElementById('id_dodge_characteristics').disabled = true;
document.getElementById('id_drive_characteristics').disabled = true;
document.getElementById('id_endurance_characteristics').disabled = true;
document.getElementById('id_entertain_characteristics').disabled = true;
document.getElementById('id_gamble_characteristics').disabled = true;
document.getElementById('id_gossip_characteristics').disabled = true;
document.getElementById('id_haggle_characteristics').disabled = true;
document.getElementById('id_intimidate_characteristics').disabled = true;
document.getElementById('id_intuition_characteristics').disabled = true;
document.getElementById('id_leadership_characteristics').disabled = true;
document.getElementById('id_melee_basic_characteristics').disabled = true;
document.getElementById('id_melee_characteristics').disabled = true;
document.getElementById('id_navigation_characteristics').disabled = true;
document.getElementById('id_outdoor_survival_characteristics').disabled = true;
document.getElementById('id_perception_characteristics').disabled = true;
document.getElementById('id_ride_characteristics').disabled = true;
document.getElementById('id_row_characteristics').disabled = true;
document.getElementById('id_stealth_characteristics').disabled = true;


document.addEventListener('DOMContentLoaded', function() {

    const wsInit = document.getElementById("id_WS_initial");
    const wsAdv = document.getElementById("id_WS_advances");
    const wsCurrent = document.getElementById("id_WS_current");

    const bsInit = document.getElementById("id_BS_initial");
    const bsAdv = document.getElementById("id_BS_advances");
    const bsCurrent = document.getElementById("id_BS_current");

    const sInit = document.getElementById("id_S_initial");
    const sAdv = document.getElementById("id_S_advances");
    const sCurrent = document.getElementById("id_S_current");

    const tInit = document.getElementById("id_T_initial");
    const tAdv = document.getElementById("id_T_advances");
    const tCurrent = document.getElementById("id_T_current");

    const iInit = document.getElementById("id_I_initial");
    const iAdv = document.getElementById("id_I_advances");
    const iCurrent = document.getElementById("id_I_current");

    const agInit = document.getElementById("id_Ag_initial");
    const agAdv = document.getElementById("id_Ag_advances");
    const agCurrent = document.getElementById("id_Ag_current");

    const dexInit = document.getElementById("id_Dex_initial");
    const dexAdv = document.getElementById("id_Dex_advances");
    const dexCurrent = document.getElementById("id_Dex_current");

    const intInit = document.getElementById("id_Int_initial");
    const intAdv = document.getElementById("id_Int_advances");
    const intCurrent = document.getElementById("id_Int_current");

    const wpInit = document.getElementById("id_WP_initial");
    const wpAdv = document.getElementById("id_WP_advances");
    const wpCurrent = document.getElementById("id_WP_current");

    const felInit = document.getElementById("id_Fel_initial");
    const felAdv = document.getElementById("id_Fel_advances");
    const felCurrent = document.getElementById("id_Fel_current");

    const artInit = document.getElementById("id_art_characteristics");

    const athInit = document.getElementById("id_athletics_characteristics");

    const briInit = document.getElementById("id_bribery_characteristics");

    const chaInit = document.getElementById("id_charm_characteristics");

    const chaaniInit = document.getElementById("id_charm_animal_characteristics");

    const cliInit = document.getElementById("id_climb_characteristics");

    const coolInit = document.getElementById("id_cool_characteristics");

    const conalcInit = document.getElementById("id_consume_alcohol_characteristics");

    const dodInit = document.getElementById("id_dodge_characteristics");

    const driInit = document.getElementById("id_drive_characteristics");

    const endInit = document.getElementById("id_endurance_characteristics");

    const entInit = document.getElementById("id_entertain_characteristics");

    const gamInit = document.getElementById("id_gamble_characteristics");

    const gosInit = document.getElementById("id_gossip_characteristics");

    const hagInit = document.getElementById("id_haggle_characteristics");

    const indInit = document.getElementById("id_intimidate_characteristics");

    const inuInit = document.getElementById("id_intuition_characteristics");

    const leaInit = document.getElementById("id_leadership_characteristics");

    const melbasInit = document.getElementById("id_melee_basic_characteristics");

    const melInit = document.getElementById("id_melee_characteristics");

    const navInit = document.getElementById("id_navigation_characteristics");

    const outsurInit = document.getElementById("id_outdoor_survival_characteristics");

    const perInit = document.getElementById("id_perception_characteristics");

    const ridInit = document.getElementById("id_ride_characteristics");

    const rowInit = document.getElementById("id_row_characteristics");

    const steInit = document.getElementById("id_stealth_characteristics");

    function updateCurrent(current, init, adv, ...extraFields) {
        const initVal = parseInt(init.value) || 0;
        const advVal = parseInt(adv.value) || 0;
        current.value = initVal + advVal;

        for (var i = 0; i < extraFields.length; i++) {
            extraFields[i].value = current.value;
        }
    }

    wsInit.addEventListener("input", updateCurrent.bind(null, wsCurrent, wsInit, wsAdv, melbasInit, melInit));
    wsAdv.addEventListener("input", updateCurrent.bind(null, wsCurrent, wsInit, wsAdv, melbasInit, melInit));

    bsInit.addEventListener("input", updateCurrent.bind(null, bsCurrent, bsInit, bsAdv));
    bsAdv.addEventListener("input", updateCurrent.bind(null, bsCurrent, bsInit, bsAdv));

    sInit.addEventListener("input", updateCurrent.bind(null, sCurrent, sInit, sAdv, cliInit, indInit, rowInit));
    sAdv.addEventListener("input", updateCurrent.bind(null, sCurrent, sInit, sAdv, cliInit, indInit, rowInit));

    tInit.addEventListener("input", updateCurrent.bind(null, tCurrent, tInit, tAdv, conalcInit, endInit));
    tAdv.addEventListener("input", updateCurrent.bind(null, tCurrent, tInit, tAdv, conalcInit, endInit));

    iInit.addEventListener("input", updateCurrent.bind(null, iCurrent, iInit, iAdv, inuInit, navInit, perInit));
    iAdv.addEventListener("input", updateCurrent.bind(null, iCurrent, iInit, iAdv, inuInit, navInit, perInit));

    agInit.addEventListener("input", updateCurrent.bind(null, agCurrent, agInit, agAdv, athInit, dodInit, driInit, ridInit, steInit));
    agAdv.addEventListener("input", updateCurrent.bind(null, agCurrent, agInit, agAdv, athInit, dodInit, driInit, ridInit, steInit));

    dexInit.addEventListener("input", updateCurrent.bind(null, dexCurrent, dexInit, dexAdv, artInit));
    dexAdv.addEventListener("input", updateCurrent.bind(null, dexCurrent, dexInit, dexAdv, artInit));

    intInit.addEventListener("input", updateCurrent.bind(null, intCurrent, intInit, intAdv, gamInit, outsurInit));
    intAdv.addEventListener("input", updateCurrent.bind(null, intCurrent, intInit, intAdv, gamInit, outsurInit));

    wpInit.addEventListener("input", updateCurrent.bind(null, wpCurrent, wpInit, wpAdv, chaaniInit, coolInit));
    wpAdv.addEventListener("input", updateCurrent.bind(null, wpCurrent, wpInit, wpAdv, chaaniInit, coolInit));

    felInit.addEventListener("input", updateCurrent.bind(null, felCurrent, felInit, felAdv, briInit, chaInit, entInit, gosInit, hagInit, leaInit));
    felAdv.addEventListener("input", updateCurrent.bind(null, felCurrent, felInit, felAdv, briInit, chaInit, entInit, gosInit, hagInit, leaInit));


});