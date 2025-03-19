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
    artInit.readOnly = true;
    artCurrent.readOnly = true;

    const athInit = document.getElementById("id_athletics_characteristics");
    const athAdv = document.getElementById("id_athletics_advances");
    const athCurrent = document.getElementById("id_athletics_skill");
    athInit.readOnly = true;
    athCurrent.readOnly = true;

    const briInit = document.getElementById("id_bribery_characteristics");
    const briAdv = document.getElementById("id_bribery_advances");
    const briCurrent = document.getElementById("id_bribery_skill");
    briInit.readOnly = true;
    briCurrent.readOnly = true;

    const chaInit = document.getElementById("id_charm_characteristics");
    const chaAdv = document.getElementById("id_charm_advances");
    const chaCurrent = document.getElementById("id_charm_skill");
    chaInit.readOnly = true;
    chaCurrent.readOnly = true;

    const chaaniInit = document.getElementById("id_charm_animal_characteristics");
    const chaaniAdv = document.getElementById("id_charm_animal_advances");
    const chaaniCurrent = document.getElementById("id_charm_animal_skill");
    chaaniInit.readOnly = true;
    chaaniCurrent.readOnly = true;

    const cliInit = document.getElementById("id_climb_characteristics");
    const cliAdv = document.getElementById("id_climb_advances");
    const cliCurrent = document.getElementById("id_climb_skill");
    cliInit.readOnly = true;
    cliCurrent.readOnly = true;

    const coolInit = document.getElementById("id_cool_characteristics");
    const coolAdv = document.getElementById("id_cool_advances");
    const coolCurrent = document.getElementById("id_cool_skill");
    coolInit.readOnly = true;
    coolCurrent.readOnly = true;

    const conalcInit = document.getElementById("id_consume_alcohol_characteristics");
    const conalcAdv = document.getElementById("id_consume_alcohol_advances");
    const conalcCurrent = document.getElementById("id_consume_alcohol_skill");
    conalcInit.readOnly = true;
    conalcCurrent.readOnly = true;

    const dodInit = document.getElementById("id_dodge_characteristics");
    const dodAdv = document.getElementById("id_dodge_advances");
    const dodCurrent = document.getElementById("id_dodge_skill");
    dodInit.readOnly = true;
    dodCurrent.readOnly = true;

    const driInit = document.getElementById("id_drive_characteristics");
    const driAdv = document.getElementById("id_drive_advances");
    const driCurrent = document.getElementById("id_drive_skill");
    driInit.readOnly = true;
    driCurrent.readOnly = true;

    const endInit = document.getElementById("id_endurance_characteristics");
    const endAdv = document.getElementById("id_endurance_advances");
    const endCurrent = document.getElementById("id_endurance_skill");
    endInit.readOnly = true;
    endCurrent.readOnly = true;

    const entInit = document.getElementById("id_entertain_characteristics");
    const entAdv = document.getElementById("id_entertain_advances");
    const entCurrent = document.getElementById("id_entertain_skill");
    entInit.readOnly = true;
    entCurrent.readOnly = true;

    const gamInit = document.getElementById("id_gamble_characteristics");
    const gamAdv = document.getElementById("id_gamble_advances");
    const gamCurrent = document.getElementById("id_gamble_skill");
    gamInit.readOnly = true;
    gamCurrent.readOnly = true;

    const gosInit = document.getElementById("id_gossip_characteristics");
    const gosAdv = document.getElementById("id_gossip_advances");
    const gosCurrent = document.getElementById("id_gossip_skill");
    gosInit.readOnly = true;
    gosCurrent.readOnly = true;

    const hagInit = document.getElementById("id_haggle_characteristics");
    const hagAdv = document.getElementById("id_haggle_advances");
    const hagCurrent = document.getElementById("id_haggle_skill");
    hagInit.readOnly = true;
    hagCurrent.readOnly = true;

    const indInit = document.getElementById("id_intimidate_characteristics");
    const indAdv = document.getElementById("id_intimidate_advances");
    const indCurrent = document.getElementById("id_intimidate_skill");
    indInit.readOnly = true;
    indCurrent.readOnly = true;

    const inuInit = document.getElementById("id_intuition_characteristics");
    const inuAdv = document.getElementById("id_intuition_advances");
    const inuCurrent = document.getElementById("id_intuition_skill");
    inuInit.readOnly = true;
    inuCurrent.readOnly = true;

    const leaInit = document.getElementById("id_leadership_characteristics");
    const leaAdv = document.getElementById("id_leadership_advances");
    const leaCurrent = document.getElementById("id_leadership_skill");
    leaInit.readOnly = true;
    leaCurrent.readOnly = true;

    const melbasInit = document.getElementById("id_melee_basic_characteristics");
    const melbasAdv = document.getElementById("id_melee_basic_advances");
    const melbasCurrent = document.getElementById("id_melee_basic_skill");
    melbasInit.readOnly = true;
    melbasCurrent.readOnly = true;

    const melInit = document.getElementById("id_melee_characteristics");
    const melAdv = document.getElementById("id_melee_advances");
    const melCurrent = document.getElementById("id_melee_skill");
    melInit.readOnly = true;
    melCurrent.readOnly = true;

    const navInit = document.getElementById("id_navigation_characteristics");
    const navAdv = document.getElementById("id_navigation_advances");
    const navCurrent = document.getElementById("id_navigation_skill");
    navInit.readOnly = true;
    navCurrent.readOnly = true;

    const outsurInit = document.getElementById("id_outdoor_survival_characteristics");
    const outsurAdv = document.getElementById("id_outdoor_survival_advances");
    const outsurCurrent = document.getElementById("id_outdoor_survival_skill");
    outsurInit.readOnly = true;
    outsurCurrent.readOnly = true;

    const perInit = document.getElementById("id_perception_characteristics");
    const perAdv = document.getElementById("id_perception_advances");
    const perCurrent = document.getElementById("id_perception_skill");
    perInit.readOnly = true;
    perCurrent.readOnly = true;

    const ridInit = document.getElementById("id_ride_characteristics");
    const ridAdv = document.getElementById("id_ride_advances");
    const ridCurrent = document.getElementById("id_ride_skill");
    ridInit.readOnly = true;
    ridCurrent.readOnly = true;

    const rowInit = document.getElementById("id_row_characteristics");
    const rowAdv = document.getElementById("id_row_advances");
    const rowCurrent = document.getElementById("id_row_skill");
    rowInit.readOnly = true;
    rowCurrent.readOnly = true;

    const steInit = document.getElementById("id_stealth_characteristics");
    const steAdv = document.getElementById("id_stealth_advances");
    const steCurrent = document.getElementById("id_stealth_skill");
    steInit.readOnly = true;
    steCurrent.readOnly = true;

    /* Wounds fields */

    const sBonus = document.getElementById("id_sb");
    sBonus.readOnly = true;

    const tBonus = document.getElementById("id_tb_x2");
    tBonus.readOnly = true;

    const wpBonus = document.getElementById("id_wbp");
    wpBonus.readOnly = true;

    const hardyTalent = document.getElementById("id_hardy");

    const woundsNumber = document.getElementById("id_wounds");
    woundsNumber.readOnly = true;

    function updateCurrent(current, init, adv, ...extraFields) {
    /* Function for characteristics calculation, also saves the values to related basic skills. */
        const initVal = parseInt(init.value) || 0;
        const advVal = parseInt(adv.value) || 0;
        current.value = initVal + advVal;

        for (var i = 0; i < extraFields.length; i++) {
            extraFields[i].value = current.value;
        }
    }

    function updateBonus(current, bonus) {
        const c = parseInt(current.value) || 0;
        if (c < 10) {
            bonus.value = 0;
        }
        else if (c > 99) {
            bonus.value = 9;
        }
        else {
            bonus.value = Number(String(c)[0]);
        }

    }

    wsInit.addEventListener("input", updateCurrent.bind(null, wsCurrent, wsInit, wsAdv, melbasInit, melInit));
    wsAdv.addEventListener("input", updateCurrent.bind(null, wsCurrent, wsInit, wsAdv, melbasInit, melInit));

    bsInit.addEventListener("input", updateCurrent.bind(null, bsCurrent, bsInit, bsAdv));
    bsAdv.addEventListener("input", updateCurrent.bind(null, bsCurrent, bsInit, bsAdv));

    sInit.addEventListener("input", () => {
        updateCurrent(sCurrent, sInit, sAdv, cliInit, indInit, rowInit);
        updateBonus(sCurrent, sBonus);
    });

    sAdv.addEventListener("input", () => {
        updateCurrent(sCurrent, sInit, sAdv, cliInit, indInit, rowInit);
        updateBonus(sCurrent, sBonus);
    });

    tInit.addEventListener("input", () => {
        updateCurrent(tCurrent, tInit, tAdv, conalcInit, endInit, tBonus)
        updateBonus(tCurrent, tBonus);
    });

    tAdv.addEventListener("input", () => {
        updateCurrent(tCurrent, tInit, tAdv, conalcInit, endInit, tBonus)
        updateBonus(tCurrent, tBonus);
    });

    iInit.addEventListener("input", updateCurrent.bind(null, iCurrent, iInit, iAdv, inuInit, navInit, perInit));
    iAdv.addEventListener("input", updateCurrent.bind(null, iCurrent, iInit, iAdv, inuInit, navInit, perInit));

    agInit.addEventListener("input", updateCurrent.bind(null, agCurrent, agInit, agAdv, athInit, dodInit, driInit, ridInit, steInit));
    agAdv.addEventListener("input", updateCurrent.bind(null, agCurrent, agInit, agAdv, athInit, dodInit, driInit, ridInit, steInit));

    dexInit.addEventListener("input", updateCurrent.bind(null, dexCurrent, dexInit, dexAdv, artInit));
    dexAdv.addEventListener("input", updateCurrent.bind(null, dexCurrent, dexInit, dexAdv, artInit));

    intInit.addEventListener("input", updateCurrent.bind(null, intCurrent, intInit, intAdv, gamInit, outsurInit));
    intAdv.addEventListener("input", updateCurrent.bind(null, intCurrent, intInit, intAdv, gamInit, outsurInit));

    wpInit.addEventListener("input", updateCurrent.bind(null, wpCurrent, wpInit, wpAdv, chaaniInit, coolInit, wpBonus));
    wpAdv.addEventListener("input", updateCurrent.bind(null, wpCurrent, wpInit, wpAdv, chaaniInit, coolInit, wpBonus));

    felInit.addEventListener("input", updateCurrent.bind(null, felCurrent, felInit, felAdv, briInit, chaInit, entInit, gosInit, hagInit, leaInit));
    felAdv.addEventListener("input", updateCurrent.bind(null, felCurrent, felInit, felAdv, briInit, chaInit, entInit, gosInit, hagInit, leaInit));

    function updateSkill(current, init, adv) {
    /* Function for basic skills final value calculation. */
        const initVal = parseInt(init.value) || 0;
        const advVal = parseInt(adv.value) || 0;
        current.value = initVal + advVal;
    }

    artAdv.addEventListener("input", updateSkill.bind(null, artCurrent, artInit, artAdv));
    athAdv.addEventListener("input", updateSkill.bind(null, athCurrent, athInit, athAdv));
    briAdv.addEventListener("input", updateSkill.bind(null, briCurrent, briInit, briAdv));
    chaAdv.addEventListener("input", updateSkill.bind(null, chaCurrent, chaInit, chaAdv));
    chaaniAdv.addEventListener("input", updateSkill.bind(null, chaaniCurrent, chaaniInit, chaaniAdv));
    cliAdv.addEventListener("input", updateSkill.bind(null, cliCurrent, cliInit, cliAdv));
    coolAdv.addEventListener("input", updateSkill.bind(null, coolCurrent, coolInit, coolAdv));
    conalcAdv.addEventListener("input", updateSkill.bind(null, conalcCurrent, conalcInit, conalcAdv));
    dodAdv.addEventListener("input", updateSkill.bind(null, dodCurrent, dodInit, dodAdv));
    driAdv.addEventListener("input", updateSkill.bind(null, driCurrent, driInit, driAdv));
    endAdv.addEventListener("input", updateSkill.bind(null, endCurrent, endInit, endAdv));
    entAdv.addEventListener("input", updateSkill.bind(null, entCurrent, entInit, entAdv));
    gamAdv.addEventListener("input", updateSkill.bind(null, gamCurrent, gamInit, gamAdv));
    gosAdv.addEventListener("input", updateSkill.bind(null, gosCurrent, gosInit, gosAdv));
    hagAdv.addEventListener("input", updateSkill.bind(null, hagCurrent, hagInit, hagAdv));
    indAdv.addEventListener("input", updateSkill.bind(null, indCurrent, indInit, indAdv));
    inuAdv.addEventListener("input", updateSkill.bind(null, inuCurrent, inuInit, inuAdv));
    leaAdv.addEventListener("input", updateSkill.bind(null, leaCurrent, leaInit, leaAdv));
    melbasAdv.addEventListener("input", updateSkill.bind(null, melbasCurrent, melbasInit, melbasAdv));
    melAdv.addEventListener("input", updateSkill.bind(null, melCurrent, melInit, melAdv));
    navAdv.addEventListener("input", updateSkill.bind(null, navCurrent, navInit, navAdv));
    outsurAdv.addEventListener("input", updateSkill.bind(null, outsurCurrent, outsurInit, outsurAdv));
    perAdv.addEventListener("input", updateSkill.bind(null, perCurrent, perInit, perAdv));
    ridAdv.addEventListener("input", updateSkill.bind(null, ridCurrent, ridInit, ridAdv));
    rowAdv.addEventListener("input", updateSkill.bind(null, rowCurrent, rowInit, rowAdv));
    steAdv.addEventListener("input", updateSkill.bind(null, steCurrent, steInit, steAdv));


    function updateWounds(sBonus, tBonus, wpBonus, hardyTalent, woundsNumber) {
    /* Function for calculation of total number of wounds (health). */
        const s = parseInt(sBonus.value) || 0;
        const t_x = parseInt(tBonus.value) || 0;
        const wp = parseInt(wpBonus.value) || 0;
        const h = parseInt(hardyTalent.value) || 0;
        woundsNumber.value = 0;
    }


});