class Locator():
    'The class contains all base locators'

    #----FIELDS----
    email = "//input[@name='email']"
    password = "//input[@name='password']"
    new_password = "//input[@id='newPassword']"
    confirm_password = "//input[@id='confirmPassword']"
    select_box = "//div[@test-id='select-box']/div"
    dropdown_list_item = select_box+"/div[2]/div/div"
    type_text = "//input[@type='text']"

    #----BUTTONS----
    enter_here = "//button[@id='redirectButton']"
    add_button = "//button[@id='item-action-add']"
    submit_button = "//button[@type='submit']"
    button_type = "//button[@type='button']"
    role_button = "//div[@role='button']"
    select_button = "//button[@data-testid='select-button']"
    button_last_page = "//button[@aria-label='Go to last page']"
    button_tab = "//button[@role='tab']"
    action_button = "//button[@data-testid='action-button']"
    item_action_customer_add = "//button[@id='item-action-customer-add']"
    filter_button = f"{button_type}//*[text()='Filter']"
    filter_input = "//div[@data-type='filter']//input"
    drop_down_button = "//button[@id='dropDownButton']"
    confirm_button = "//button[@data-testid='confirm-button']"
    continue_import = "//button/span[text()='Continue import']"
    button_save = "//button[@label='Save']"
    save_button = "//button/span[text()='Save']"
    cancel_button = "//button[@label='Cancel']"
    close_button = "//button[@data-testid='close-button']"
    label_confirm = "//button[@label='Confirm']"
    label_cancel = "//button[@label='Cancel']"
    ping_to_return = "//span[text()='Request to return']/../../button"
    edit_button = "//button[@data-testid='edit-button']"
    remove_button = "//button[@data-testid='remove-button']"
    planogram_button = "//button[@data-testid='planogram-button']"
    unassign_button = "//button[@data-testid='unassign-button']"
    customer_info_button = "//button[@data-testid='customer-info-button']"
    shipto_info_button = "//button[@data-testid='shipto-info-button']"
    associated_shiptos = "//button[@data-testid='associated-shiptos-button']"
    associated_users = "//button[@data-testid='associated-users-button']"
    configure_button = "//button[@data-testid='configure-button']"
    view_button = "//button[@data-testid='view-button']"
    edit_status_button = "//button[@data-testid='edit-status-button']"
    split_button = "//button[@data-testid='split-button']"
    complete_button = "//button/span[text()='Complete']"
    sign_out = "//div[text()='Sign Out']"
    actions_button = "//button[@data-testid='sticky-last-more-button']"
    button_reset = "//button[@type='reset']"
    info_button = "//button[@data-testid='info-button']"

    #----TABLE----
    table_row = "//div[@role='rowgroup']"
    role_row = "//div[@role='row']"
    table_column = "//div[@role='gridcell']"
    role_cell = "//div[@role='cell']"
    old_table = "//div[@class='rt-table' and @role='grid' and @data-page-count]"
    role_table = "//div[@role='table' and @data-page-count]"
    last_role_row = f"({role_row})[last()]"
    table_header_column = "//div[@role='columnheader']"

    #----OTHERS----
    forgot_password = "//a[text()='Reset my password']"
    reset_password = "//div[text()='Reset password']"
    dialog = "//div[@role='dialog']"
    role_listbox = "//ul[@role='listbox']"
    file_upload = "//input[@id='file-upload']"
    upload_rfid_csv = "//input[@id='upload-rfid-csv']"
    upload_rfid_available = "//input[@id='upload-rfid-available']"
    item_action_import = "//button[@id='item-action-import']"
    forgot_password = "//a[text()='Reset my password']"
    checkbox = "//input[@type='checkbox']"
    pagination_bottom = "//div[@class='pagination-bottom']"
    pagination_navigation = "//nav[@aria-label='pagination navigation']"
    successfully_imported_msg = "//span[@id='client-snackbar']//strong[text()='Successfully imported']"
    successfully_uploaded_document_msg = "//span[text()='Document uploaded successfully!']"
    successfully_submitted_reorder_list = "//span[text()='Reorder list was successfully submitted']"
    no_data_found = "//div[text()='No data found']"
    progress_bar = "//div[@role='progressbar']"
    role_menu = "//ul[@role='menu']"
    role_menuitem = "//li[@role='menuitem']"
    check_mark = "//span[text()='???']"
    listbox = "//div[@aria-haspopup='listbox']/.."

    @staticmethod
    def get_indexed(xpath, index):
        return f"({xpath})[{index}]"

    @staticmethod
    def get_dropdown_in_dialog(index):
        return Locator.get_indexed(Locator.select_box, index)

    @staticmethod
    def get_checkbox_in_dialog_by_name(name):
        return f"{Locator.dialog}//span[text()='{name}']/..//input[@type='checkbox']"

    @staticmethod
    def get_button_tab_by_name(name):
        return f"{Locator.button_tab}//span[text()='{name}']"

    @staticmethod
    def get_table_item_outdated(row, column, sub_xpath=""):
        return f"(({sub_xpath}{Locator.table_row})[{row}]{Locator.table_column})[{column}]"

    @staticmethod
    def get_table_item(row, column):
        return f"(({Locator.role_row})[{row}]{Locator.role_cell})[{column}]"

    @staticmethod
    def get_last_table_item(column):
        return f"(({Locator.role_row})[last()]{Locator.role_cell})[{column}]"

    @staticmethod
    def get_last_table_item_outdated(column):
        return f"(({Locator.role_row})[last()]{Locator.table_column})[{column}]"

    @staticmethod
    def get_table_item_by_index(index, column, page=None):
        if page is None:
            return f"(//div[@role='row' and @data-row-index='{index}']{Locator.role_cell})[{column}]"
        return f"(//div[@role='row' and @data-row-index='{index}' and @data-page-index='{page}']{Locator.role_cell})[{column}]"

    @staticmethod
    def get_table_item_by_index_outdated(index, column, page):
        return f"//div[@role='row' and @index='{index}' and @data-page-index='{page}']{Locator.table_column}[{column}]"

    @staticmethod
    def get_table_item_in_dialog(row, column):
        return f"(({Locator.dialog}{Locator.table_row})[{row}]{Locator.table_column})[{column}]"

    @staticmethod
    def get_button_by_name(name):
        return f"{Locator.button_type}//span[text()='{name}']"

    @staticmethod
    def get_planogram(door, cell):
        return f"//div[@data-door='{door}']//div[@data-cell='{cell}']"

    @staticmethod
    def get_dropdown_sku(sku):
        return f"{Locator.dropdown_list_item}//span[text()='{sku}']/../.."

    @staticmethod
    def get_select_pagination(value):
        return f"{Locator.role_listbox}/li[@data-value='{value}']"

    @staticmethod
    def get_menuitem_with_text(text):
        return f"//li[@role='menuitem' and text()='{text}']"

    def __setattr__(self, key, value):
        if hasattr(key):
            object.__setattr__(key, value)
        else:
            raise TypeError("Cannot create new attribute for class Locator")
