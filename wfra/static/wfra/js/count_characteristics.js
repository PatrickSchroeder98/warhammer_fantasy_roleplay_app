document.addEventListener('DOMContentLoaded', function() {

    /* Characteristics fields */

    const wsInit = document.getElementById("id_WS_initial");
    const wsAdv = document.getElementById("id_WS_advances");
    const wsCurrent = document.getElementById("id_WS_current");
    wsCurrent.disabled = true;

    const bsInit = document.getElementById("id_BS_initial");
    const bsAdv = document.getElementById("id_BS_advances");
    const bsCurrent = document.getElementById("id_BS_current");
    bsCurrent.disabled = true;

    const sInit = document.getElementById("id_S_initial");
    const sAdv = document.getElementById("id_S_advances");
    const sCurrent = document.getElementById("id_S_current");
    sCurrent.disabled = true;

    const tInit = document.getElementById("id_T_initial");
    const tAdv = document.getElementById("id_T_advances");
    const tCurrent = document.getElementById("id_T_current");
    tCurrent.disabled = true;

    const iInit = document.getElementById("id_I_initial");
    const iAdv = document.getElementById("id_I_advances");
    const iCurrent = document.getElementById("id_I_current");
    iCurrent.disabled = true;

    const agInit = document.getElementById("id_Ag_initial");
    const agAdv = document.getElementById("id_Ag_advances");
    const agCurrent = document.getElementById("id_Ag_current");
    agCurrent.disabled = true;

    const dexInit = document.getElementById("id_Dex_initial");
    const dexAdv = document.getElementById("id_Dex_advances");
    const dexCurrent = document.getElementById("id_Dex_current");
    dexCurrent.disabled = true;

    const intInit = document.getElementById("id_Int_initial");
    const intAdv = document.getElementById("id_Int_advances");
    const intCurrent = document.getElementById("id_Int_current");
    intCurrent.disabled = true;

    const wpInit = document.getElementById("id_WP_initial");
    const wpAdv = document.getElementById("id_WP_advances");
    const wpCurrent = document.getElementById("id_WP_current");
    wpCurrent.disabled = true;

    const felInit = document.getElementById("id_Fel_initial");
    const felAdv = document.getElementById("id_Fel_advances");
    const felCurrent = document.getElementById("id_Fel_current");
    felCurrent.disabled = true;

    /* Basic Skills fields */

    const artInit = document.getElementById("id_art_characteristics");
    const artAdv = document.getElementById("id_art_advances");
    const artCurrent = document.getElementById("id_art_skill");
    artInit.disabled = true;
    artCurrent.disabled = true;

    const athInit = document.getElementById("id_athletics_characteristics");
    const athAdv = document.getElementById("id_athletics_advances");
    const athCurrent = document.getElementById("id_athletics_skill");
    athInit.disabled = true;
    athCurrent.disabled = true;

    const briInit = document.getElementById("id_bribery_characteristics");
    const briAdv = document.getElementById("id_bribery_advances");
    const briCurrent = document.getElementById("id_bribery_skill");
    briInit.disabled = true;
    briCurrent.disabled = true;

    const chaInit = document.getElementById("id_charm_characteristics");
    const chaAdv = document.getElementById("id_charm_advances");
    const chaCurrent = document.getElementById("id_charm_skill");
    chaInit.disabled = true;
    chaCurrent.disabled = true;

    const chaaniInit = document.getElementById("id_charm_animal_characteristics");
    const chaaniAdv = document.getElementById("id_charm_animal_advances");
    const chaaniCurrent = document.getElementById("id_charm_animal_skill");
    chaaniInit.disabled = true;
    chaaniCurrent.disabled = true;

    const cliInit = document.getElementById("id_climb_characteristics");
    const cliAdv = document.getElementById("id_climb_advances");
    const cliCurrent = document.getElementById("id_climb_skill");
    cliInit.disabled = true;
    cliCurrent.disabled = true;

    const coolInit = document.getElementById("id_cool_characteristics");
    const coolAdv = document.getElementById("id_cool_advances");
    const coolCurrent = document.getElementById("id_cool_skill");
    coolInit.disabled = true;
    coolCurrent.disabled = true;

    const conalcInit = document.getElementById("id_consume_alcohol_characteristics");
    const conalcAdv = document.getElementById("id_consume_alcohol_advances");
    const conalcCurrent = document.getElementById("id_consume_alcohol_skill");
    conalcInit.disabled = true;
    conalcCurrent.disabled = true;

    const dodInit = document.getElementById("id_dodge_characteristics");
    const dodAdv = document.getElementById("id_dodge_advances");
    const dodCurrent = document.getElementById("id_dodge_skill");
    dodInit.disabled = true;
    dodCurrent.disabled = true;

    const driInit = document.getElementById("id_drive_characteristics");
    const driAdv = document.getElementById("id_drive_advances");
    const driCurrent = document.getElementById("id_drive_skill");
    driInit.disabled = true;
    driCurrent.disabled = true;

    const endInit = document.getElementById("id_endurance_characteristics");
    const endAdv = document.getElementById("id_endurance_advances");
    const endCurrent = document.getElementById("id_endurance_skill");
    endInit.disabled = true;
    endCurrent.disabled = true;

    const entInit = document.getElementById("id_entertain_characteristics");
    const entAdv = document.getElementById("id_entertain_advances");
    const entCurrent = document.getElementById("id_entertain_skill");
    entInit.disabled = true;
    entCurrent.disabled = true;

    const gamInit = document.getElementById("id_gamble_characteristics");
    const gamAdv = document.getElementById("id_gamble_advances");
    const gamCurrent = document.getElementById("id_gamble_skill");
    gamInit.disabled = true;
    gamCurrent.disabled = true;

    const gosInit = document.getElementById("id_gossip_characteristics");
    const gosAdv = document.getElementById("id_gossip_advances");
    const gosCurrent = document.getElementById("id_gossip_skill");
    gosInit.disabled = true;
    gosCurrent.disabled = true;

    const hagInit = document.getElementById("id_haggle_characteristics");
    const hagAdv = document.getElementById("id_haggle_advances");
    const hagCurrent = document.getElementById("id_haggle_skill");
    hagInit.disabled = true;
    hagCurrent.disabled = true;

    const indInit = document.getElementById("id_intimidate_characteristics");
    const indAdv = document.getElementById("id_intimidate_advances");
    const indCurrent = document.getElementById("id_intimidate_skill");
    indInit.disabled = true;
    indCurrent.disabled = true;

    const inuInit = document.getElementById("id_intuition_characteristics");
    const inuAdv = document.getElementById("id_intuition_advances");
    const inuCurrent = document.getElementById("id_intuition_skill");
    inuInit.disabled = true;
    inuCurrent.disabled = true;

    const leaInit = document.getElementById("id_leadership_characteristics");
    const leaAdv = document.getElementById("id_leadership_advances");
    const leaCurrent = document.getElementById("id_leadership_skill");
    leaInit.disabled = true;
    leaCurrent.disabled = true;

    const melbasInit = document.getElementById("id_melee_basic_characteristics");
    const melbasAdv = document.getElementById("id_melee_basic_advances");
    const melbasCurrent = document.getElementById("id_melee_basic_skill");
    melbasInit.disabled = true;
    melbasCurrent.disabled = true;

    const melInit = document.getElementById("id_melee_characteristics");
    const melAdv = document.getElementById("id_melee_advances");
    const melCurrent = document.getElementById("id_melee_skill");
    melInit.disabled = true;
    melCurrent.disabled = true;

    const navInit = document.getElementById("id_navigation_characteristics");
    const navAdv = document.getElementById("id_navigation_advances");
    const navCurrent = document.getElementById("id_navigation_skill");
    navInit.disabled = true;
    navCurrent.disabled = true;

    const outsurInit = document.getElementById("id_outdoor_survival_characteristics");
    const outsurAdv = document.getElementById("id_outdoor_survival_advances");
    const outsurCurrent = document.getElementById("id_outdoor_survival_skill");
    outsurInit.disabled = true;
    outsurCurrent.disabled = true;

    const perInit = document.getElementById("id_perception_characteristics");
    const perAdv = document.getElementById("id_perception_advances");
    const perCurrent = document.getElementById("id_perception_skill");
    perInit.disabled = true;
    perCurrent.disabled = true;

    const ridInit = document.getElementById("id_ride_characteristics");
    const ridAdv = document.getElementById("id_ride_advances");
    const ridCurrent = document.getElementById("id_ride_skill");
    ridInit.disabled = true;
    ridCurrent.disabled = true;

    const rowInit = document.getElementById("id_row_characteristics");
    const rowAdv = document.getElementById("id_row_advances");
    const rowCurrent = document.getElementById("id_row_skill");
    rowInit.disabled = true;
    rowCurrent.disabled = true;

    const steInit = document.getElementById("id_stealth_characteristics");
    const steAdv = document.getElementById("id_stealth_advances");
    const steCurrent = document.getElementById("id_stealth_skill");
    steInit.disabled = true;
    steCurrent.disabled = true;

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

    function updateSkill(current, init, adv) {
        const initVal = parseInt(init.value) || 0;
        const advVal = parseInt(adv.value) || 0;
        current.value = initVal + advVal;
    }

    artAdv.addEventListener("input", updateSkill.bind(null, artCurrent, artInit, artAdv))
});