from django.urls import path
from . import views

app_name = 'equipment'

urlpatterns = [
    path("character/<int:character_id>/", views.CharacterEquipmentView.as_view(), name="character_equipment"),

    path("character/<int:character_id>/add-melee-weapon/", views.CreateCharacterMeleeWeaponView.as_view(), name="add_character_melee_weapon"),
    path("character/<int:character_id>/add-ranged-weapon/", views.CreateCharacterRangedWeaponView.as_view(), name="add_character_ranged_weapon"),
    path("character/<int:character_id>/add-ammunition/", views.CreateViewCharacterAmmunition.as_view(), name="add_character_ammunition"),
    path("character/<int:character_id>/add-armour/", views.CreateViewCharacterArmour.as_view(), name="add_character_armour"),

    path("character_melee_weapons/<int:pk>/edit/", views.UpdateViewCharacterMeleeWeapons.as_view(), name="edit_character_melee_weapon"),
    path("character_ranged_weapons/<int:pk>/edit/", views.UpdateViewCharacterRangedWeapons.as_view(), name="edit_character_ranged_weapon"),
    path("character_ammunition/<int:pk>/edit/", views.UpdateViewCharacterAmmunition.as_view(), name="edit_character_ammunition"),
    path("character_armour/<int:pk>/edit/", views.UpdateViewCharacterArmour.as_view(), name="edit_character_armour"),

    path("character_melee_weapons/<int:pk>/delete", views.DeleteViewCharacterMeleeWeapon.as_view(), name="delete_character_melee_weapon"),
    path("character_ranged_weapons/<int:pk>/delete", views.DeleteViewCharacterRangedWeapon.as_view(), name="delete_character_ranged_weapon"),
    path("character_ammunition/<int:pk>/delete", views.DeleteViewCharacterAmmunition.as_view(), name="delete_character_ammunition"),
    path("character_armour/<int:pk>/delete", views.DeleteViewCharacterArmour.as_view(), name="delete_character_armour"),

    path("meleeweapons/<int:pk>/", views.DetailViewMeleeWeapons.as_view(), name="detail_melee_weapon"),
    path("rangedweapons/<int:pk>/", views.DetailViewRangedWeapons.as_view(), name="detail_ranged_weapon"),
    path("ammunition/<int:pk>/", views.DetailViewAmmunition.as_view(), name="detail_ammunition"),
    path("armour/<int:pk>/", views.DetailViewArmour.as_view(), name="detail_armour"),
    path("packsandcontainers/<int:pk>/", views.DetailViewPacksAndContainers.as_view(), name="detail_packs_and_containers"),
    path("clothingandaccessories/<int:pk>/", views.DetailViewClothingAndAccessories.as_view(), name="detail_clothing_and_accessories"),
    path("fooddrinkandlodging/<int:pk>/", views.DetailViewFoodDrinkAndLodging.as_view(), name="detail_food_drink_and_lodging"),
    path("toolsandkits/<int:pk>/", views.DetailViewToolsAndKits.as_view(), name="detail_tools_and_kits"),
    path("booksanddocuments/<int:pk>/", views.DetailViewBooksAndDocuments.as_view(), name="detail_books_and_documents"),
    path("tradetoolsandworkshops/<int:pk>/", views.DetailViewTradeToolsAndWorkshops.as_view(), name="detail_trade_tools_and_workshops"),
    path("animalsandvehicles/<int:pk>/", views.DetailViewAnimalsAndVehicles.as_view(), name="detail_animals_and_vehicles"),
    path("drugsandpoisons/<int:pk>/", views.DetailViewDrugsAndPoisons.as_view(), name="detail_drugs_and_poisons"),
    path("herbsanddraughts/<int:pk>/", views.DetailViewHerbsAndDraughts.as_view(), name="detail_herbs_and_draughts"),
    path("prosthetics/<int:pk>/", views.DetailViewProsthetics.as_view(), name="detail_prosthetics"),
    path("miscellaneoustrappings/<int:pk>/", views.DetailViewMiscellaneousTrappings.as_view(), name="detail_miscellaneous_trappings"),
    path("hirelings/<int:pk>/", views.DetailViewHirelings.as_view(), name="detail_hirelings"),
]
