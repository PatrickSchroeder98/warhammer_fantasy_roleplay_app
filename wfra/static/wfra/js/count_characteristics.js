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

    function updateCurrent(current, init, adv) {
        const initVal = parseInt(init.value) || 0;
        const advVal = parseInt(adv.value) || 0;
        current.value = initVal + advVal;
    }

    tInit.addEventListener("input", updateCurrent.bind(null, tCurrent, tInit, tAdv));
    tAdv.addEventListener("input", updateCurrent.bind(null, tCurrent, tInit, tAdv));
});