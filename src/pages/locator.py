class Locator():
    'The class contains all base locators'

    #----FIELDS----
    email = "//input[@name='email']"
    password = "//input[@name='password']"
    new_password = "//input[@id='newPassword']"
    confirm_password = "//input[@id='confirmPassword']"

    #----BUTTONS----
    enter_here = "//button[@id='redirectButton']"
    add_button = "//button[@id='item-action-add']"
    submit_button = "//button[@type='submit']"
    button_type = "//button[@type='button']"
    select_button = "//button[@data-testid='select-button']"
    button_last_page = "//button[@aria-label='Go to last page']"
    button_tab = "//button[@role='tab']"
    action_button = "//button[@data-testid='action-button']"

    #----TABLE----
    table_row = "//div[@role='rowgroup']"
    role_row = "//div[@role='row']"
    table_column = "//div[@role='gridcell']"
    role_cell = "//div[@role='cell']"
    old_table = "//div[@class='rt-table' and @role='grid']"

    #----OTHERS----
    forgot_password = "//a[text()='Reset my password']"
    dialog = "//div[@role='dialog']"
    role_listbox = "//ul[@role='listbox']"

    item_action_customer_add = "//button[@id='item-action-customer-add']"
    file_upload = "//input[@id='file-upload']"
    upload_rfid_csv = "upload-rfid-csv"
    upload_rfid_available = "upload-rfid-available"
    intercom_container = "intercom-container"
    drop_down_button = "dropDownButton"
    item_action_import = "item-action-import"
    forgot_password = "//a[text()='Reset my password']"
    select_box = "//div[@test-id='select-box']/div"
    dropdown_list_item = select_box+"/div[2]/div/div"
    table_header_column = "//div[@role='columnheader']"
    table = "//div[@class='rt-table']"
    checkbox = "//input[@type='checkbox']"
    confirm_button = "//button[@data-testid='confirm-button']"
    dialog_cancel_button = "//button[@data-testid='cancel-button']"
    pagination_bottom = "//div[@class='pagination-bottom']"
    pagination_navigation = "//nav[@aria-label='pagination navigation']"
    continue_import = "//button/span[text()='Continue import']"
    successfully_imported_msg = "//span[@id='client-snackbar']//strong[text()='Successfully imported']"
    successfully_uploaded_document_msg = "//span[text()='Document uploaded successfully!']"
    successfully_submitted_reorder_list = "//span[text()='Reorder list was successfully submitted']"
    button_save = "//button[@label='Save']"
    last_role_row = f"({role_row})[last()]"
    replenishment_item = "//div[@data-testid='replenishment-item']"
    replenishment_item_sku = "//div[@data-testid='part-sku']"
    submit_reorder_list_button = "//button/span[text()='Submit']"
    save_button = "//button/span[text()='Save']"
    cancel_button = "//button[@label='Cancel']"
    type_text = "//input[@type='text']"
    assign_product_planogram = "//button[@type='button']/span[text()='ASSIGN PRODUCT']"
    no_data_found = "//div[text()='No data found']"
    close_button = "//button[@data-testid='close-button']"
    role_presentation = "//div[@role='presentation']"
    label_confirm = "//button[@label='Confirm']"
    label_cancel = "//button[@label='Cancel']"
    progress_bar = "//div[@role='progressbar']"
    issue_button = "//span[text()='Issue']/../button"
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
    role_menu = "//ul[@role='menu']"
    role_menuitem = "//li[@role='menuitem']"
    check_mark = "//span[text()='✓']"
    next = "//button/span[text()='Next']"
    complete_button = "//button/span[text()='Complete']"
    sign_out = "//div[text()='Sign Out']"
    reset_password = "//div[text()='Reset password']"
    actions_button = "//button[@data-testid='sticky-last-more-button']"
    listbox = "//div[@aria-haspopup='listbox']/.."
    reload_button = "//button[@data-testid='reload-button']"
    button_reset = "//button[@type='reset']"
    info_button = "//button[@data-testid='info-button']"

    @staticmethod
    def get_indexed(xpath, index):
        return f"({xpath})[{index}]"

    @staticmethod
    def get_checkbox_in_dialog(index):
        return Locator.get_indexed(Locator.dialog+Locator.checkbox, index)

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
    def get_row_by_index(index):
        return f"//div[@role='row' and @data-row-index='{index}']"

    @staticmethod
    def get_table_item_by_index(index, column):
        return f"//div[@role='row' and @data-row-index='{index}']{Locator.role_cell}[{column}]"

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

    def __setattr__(self, key, value):
        if hasattr(key):
            object.__setattr__(key, value)
        else:
            raise TypeError("Cannot create new attribute for class Locator")
