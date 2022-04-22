class Locator():
    'The class contains all base locators'

    email = "//input[@id='email']"
    password = "//input[@id='password']"
    enter_here = "redirectButton"
    add_button = "item-action-add"
    item_action_customer_add = "item-action-customer-add"
    file_upload = "file-upload"
    upload_rfid_csv = "upload-rfid-csv"
    upload_rfid_available = "upload-rfid-available"
    intercom_container = "intercom-container"
    drop_down_button = "dropDownButton"
    new_password = "newPassword"
    confirm_password = "confirmPassword"
    item_action_import = "item-action-import"
    forgot_password = "//a[text()='Reset my password']"
    submit_button = "//button[@type='submit']"
    dialog = "//div[@role='dialog']"
    select_box = "//div[@test-id='select-box']/div"
    dropdown_list_item = select_box+"/div[2]/div/div"
    button_tab = "//button[@role='tab']"
    table_row = "//div[@role='rowgroup']"
    table_column = "//div[@role='gridcell']"
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
    button = "//div[@role='button']"
    button_type = "//button[@type='button']"
    button_save = "//button[@label='Save']"
    role_row = "//div[@role='row']"
    last_role_row = f"({role_row})[last()]"
    role_cell = "//div[@role='cell']"
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
    select_button = "//button[@data-testid='select-button']"
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
    role_listbox = "//ul[@role='listbox']"
    button_last_page = "//button[@aria-label='Go to last page']"
    reload_button = "//button[@data-testid='reload-button']"
    button_reset = "//button[@type='reset']"

    @staticmethod
    def index(xpath, index):
        return f"({xpath})[{index}]"

    @staticmethod
    def xpath_checkbox_in_dialog(index):
        return Locator.xpath_by_count(Locator.xpath_dialog+Locator.xpath_checkbox, index)

    @staticmethod
    def xpath_dropdown_in_dialog(index):
        return Locator.xpath_by_count(Locator.xpath_select_box, index)

    @staticmethod
    def xpath_checkbox_in_dialog_by_name(name):
        return f"{Locator.xpath_dialog}//span[text()='{name}']/..//input[@type='checkbox']"

    @staticmethod
    def xpath_button_tab_by_name(name):
        return f"{Locator.xpath_button_tab}//span[text()='{name}']"

    @staticmethod
    def xpath_table_item(row, column, sub_xpath=""):
        return f"(({sub_xpath}{Locator.xpath_table_row})[{row}]{Locator.xpath_table_column})[{column}]"

    @staticmethod
    def xpath_get_table_item(row, column):
        return f"(({Locator.xpath_role_row})[{row}]{Locator.xpath_role_cell})[{column}]"

    @staticmethod
    def xpath_get_last_table_item(column):
        return f"(({Locator.xpath_role_row})[last()]{Locator.xpath_role_cell})[{column}]"

    @staticmethod
    def xpath_get_row_by_index(index):
        return f"//div[@role='row' and @data-row-index='{index}']"

    @staticmethod
    def xpath_get_table_item_by_index(index, column):
        return f"//div[@role='row' and @data-row-index='{index}']{Locator.xpath_role_cell}[{column}]"

    @staticmethod
    def xpath_table_item_in_dialog(row, column):
        return f"(({Locator.xpath_dialog}{Locator.xpath_table_row})[{row}]{Locator.xpath_table_column})[{column}]"

    @staticmethod
    def xpath_button_by_name(name):
        return f"//button[@type='button']//span[text()='{name}']"

    @staticmethod
    def xpath_planogram(door, cell):
        return f"//div[@data-door='{door}']//div[@data-cell='{cell}']"

    @staticmethod
    def xpath_dropdown_sku(sku):
        return f"{Locator.xpath_dropdown_list_item}//span[text()='{sku}']/../.."

    @staticmethod
    def xpath_select_pagination(value):
        return f"{Locator.xpath_role_listbox}/li[@data-value='{value}']"

    def __setattr__(self, key, value):
        if hasattr(key):
            object.__setattr__(key, value)
        else:
            raise TypeError("Cannot create new attribute for class Locator")
