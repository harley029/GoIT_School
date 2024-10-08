from django.urls import path
from contacts.views import (
    MainView,
    RecordDetailView,
    TagDetailView,
    AddBookView,
    AddTagView,
    AddPhoneView,
    AddContactView,
    AddRecordView,
    DeleteView,
    PhoneDeleteListView,
    PhoneDeleteConfirmView,
    TagDeleteListView,
    TagDeleteConfirmView,
    NoteDeleteListView,
    NoteDeleteConfirmView,
    ContactDeleteListView,
    ContactDeleteConfirmView,
    SearchView,
    SearchViewName,
    SearchViewPhone,
    SearchViewEmail,
    SearchViewBirthday,
    SearchViewTag,
    SearchViewUpcomingBirthdays,
    UpdateView,
    TagListView,
    update_tag,
    ContactListView,
    update_contact,
    RecordListView,
    update_note,
    PhoneNumberListView,
    update_phone_number,
)

urlpatterns = [
    path("contacts/", MainView.as_view(), name="contacts"),
    path("contacts/page/<int:page>/", MainView.as_view(), name="contacts_paginate"),
    path("contact/<str:contact_id>/", RecordDetailView.as_view(), name="contact_detail"),
    path("tag/<str:tag_name>/", TagDetailView.as_view(), name="tag_detail"),
    path("tag/<str:tag_name>/page/<int:page>/", TagDetailView.as_view(), name="tag_detail_paginate",),
    path("add-book/", AddBookView.as_view(), name="add_book"),
    path("add_tags/", AddTagView.as_view(), name="add_tag"),
    path("add-phone/", AddPhoneView.as_view(), name="add_phone"),
    path("contacts/add/", AddContactView.as_view(), name="add_contact"),
    path("contacts/add_record/", AddRecordView.as_view(), name="add_record"),
    path("delete_book/", DeleteView.as_view(), name="delete_book"),
    path("phones/delete/", PhoneDeleteListView.as_view(), name="phone_number_delete_list"),
    path("phone/<int:pk>/delete/", PhoneDeleteConfirmView.as_view(), name="phone_delete_confirm"),
    path("tags/delete/", TagDeleteListView.as_view(), name="tag_delete_list"),
    path("tag/<int:pk>/delete/", TagDeleteConfirmView.as_view(), name="tag_delete_confirm"),
    path("notes/delete/", NoteDeleteListView.as_view(), name="note_delete_list"),
    path("note/<int:pk>/delete/", NoteDeleteConfirmView.as_view(), name="note_delete_confirm"),
    path("contacts/delete/", ContactDeleteListView.as_view(), name="contact_delete_list"),
    path("contact/<int:pk>/delete/", ContactDeleteConfirmView.as_view(), name="contact_delete_confirm"),
    path("search/", SearchView.as_view(), name="main_search"),
    path('search/name/', SearchViewName.as_view(), name='search_name'),
    path('search/phone/', SearchViewPhone.as_view(), name='search_phone'),
    path('search/email/', SearchViewEmail.as_view(), name='search_email'),
    path('search/birthday/', SearchViewBirthday.as_view(), name='search_birthday'),
    path('search/tag/', SearchViewTag.as_view(), name='search_tag'),
    path('search/upcoming_birthdays/', SearchViewUpcomingBirthdays.as_view(), name='search_upcoming_birthdays'),
    path("update/", UpdateView.as_view(), name="main_update"),
    path("update/tags/", TagListView.as_view(), name="tag_list"),
    path("update/tag/<int:pk>/", update_tag, name="update_tag"),
    path("update/contacts/", ContactListView.as_view(), name="contact_list"),
    path("update/contact/<int:pk>/", update_contact, name="update_contact"),
    path("update/notes/", RecordListView.as_view(), name="note_list"),
    path("update/note/<int:pk>/", update_note, name="update_note"),
    path('phones/', PhoneNumberListView.as_view(), name='phone_number_list'),
    path('phone/<int:pk>/update/', update_phone_number, name='update_phone_number'),
]
