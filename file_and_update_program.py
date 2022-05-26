from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def file_and_update(username,password,grant,source,country,status,date,donor,budget,desc,funding_type,funding_office,submission_type,ticket_id,app_id,resilience_check,due_date,match,submitted_var,months,ceiling,start_date,role,opp_type,sect_list,donor_abbr,opp_abbr):
  driver=webdriver.Chrome("REDACTED")
  driver.get("REDACTED") #wl3 login
  sleep(3)
  driver.find_element_by_xpath('/html/body/app-root/div[2]/wl3-auth/div[2]/div[2]/div[1]/a').click()
  driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
  driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
  sleep(3)
  driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
  driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
  sleep(15)
  driver.get("REDACTED") #/#/grants/create
  sleep(8)
  driver.get("REDACTED") #/#/grants/create
  sleep(5)
  driver.find_element_by_xpath('//*[@id="name"]').send_keys(grant)
  sleep(1)
  driver.find_element_by_xpath('//*[@id="source"]').click()
  sleep(3)
  select = Select(driver.find_element_by_id('source'))
  select.select_by_visible_text(source)
  sleep(1)
  select = Select(driver.find_element_by_id('hostCountries'))
  select.select_by_visible_text(country)
  sleep(1)
  select = Select(driver.find_element_by_id('status'))
  select.select_by_visible_text(status)
  sleep(1)
  driver.find_element_by_xpath('//*[@id="statusDate"]').send_keys(date)
  sleep(1)
  driver.find_element_by_xpath('//*[@id="grantors"]').send_keys(donor)
  sleep(3)
  actions = ActionChains(driver)
  actions.send_keys('\ue015')
  actions.perform()
  actions.send_keys('\ue007')
  actions.perform()
  sleep(1)
  if resilience_check == 'Yes':
    driver.find_element_by_xpath('//*[@id="tags"]').send_keys("Resilience")
    sleep(3)
    actions = ActionChains(driver)
    actions.send_keys('\ue015')
    actions.perform()
    actions.send_keys('\ue007')
    actions.perform()
    sleep(1)
  driver.find_element_by_xpath('//*[@id="grantCreateSave"]').click()
  sleep(3)

  wl3_url = driver.current_url
  wl3_id = wl3_url[-4:]
  file_name = status + "_" + donor_abbr + "_" + opp_abbr +"_WL3:" + wl3_id
  wl3_entry_string = "The WL3 Entry for this opportunity is: " + wl3_url

  country_drive_url = {
        'Bangladesh':"REDACTED",
        'Bolivia':"REDACTED",
        'Burundi':"REDACTED",
        'Cambodia':"REDACTED",
        'DRC':"REDACTED",
        'Dominican Republic':"REDACTED",
        'Ethiopia':"REDACTED",
        'Guatemala':"REDACTED",
        'Haiti':"REDACTED",
        'Indonesia':"REDACTED",
        'Kenya':"REDACTED",
        'Mozambique':"REDACTED",
        'Nicaragua':"REDACTED",
        'Peru':"REDACTED",
        'Philippines':"REDACTED",
        'Rwanda':"REDACTED",
        'South Sudan':"REDACTED",
        'Uganda':"REDACTED"
        }
        
  file_location = country_drive_url[country]

  driver.get(file_location)
  sleep(3)
  driver.find_element_by_xpath('//*[@id="drive_main_page"]/div/div[3]/div/button[1]').click()
  sleep(2)
  actions = ActionChains(driver)
  actions.send_keys('\ue007')
  actions.perform()
  sleep(3)
  actions.send_keys(file_name)
  actions.perform()
  sleep(3)
  actions.send_keys('\ue007')
  actions.perform()
  sleep(3)
  actions.send_keys('\ue007')
  actions.perform()
  sleep(3)

  google_file_url = driver.current_url
  google_file_string = "The URL for the Google Drive Folder is: " + google_file_url

  driver.get(wl3_url)
  sleep(6)
  driver.find_element_by_xpath('//*[@id="grantProfileEdit"]').click()
  sleep(2)
  driver.find_element_by_xpath('//*[@id="totalDonorBudget"]').send_keys(budget)
  sleep(1)
  driver.find_element_by_xpath('//*[@id="grantDescription"]').send_keys(desc)
  sleep(1)
  select = Select(driver.find_element_by_id('fundingType'))
  select.select_by_visible_text(funding_type)
  sleep(1)
  if submission_type == "Concept Note":
      driver.find_element_by_xpath('//*[@id="conceptNote"]').click()
      sleep(1)
  if submission_type == "Full Proposal":
      driver.find_element_by_xpath('//*[@id="fullProposal"]').click()
      sleep(1)
  if submission_type == "Cost Extension":
      driver.find_element_by_xpath('//*[@id="costExtension"]').click()
      sleep(1)
  driver.find_element_by_xpath('//*[@id="coordinationTicket"]').send_keys(ticket_id)
  sleep(1)
  driver.find_element_by_xpath('//*[@id="approvalTicket"]').send_keys(app_id)
  sleep(1)
  driver.find_element_by_xpath('//*[@id="relatedDocuments"]').send_keys(google_file_url)
  sleep(1)
  driver.find_element_by_xpath('//*[@id="grantProfileUpdateSave"]').click()
  sleep(3)
  driver.get(wl3_url)
  sleep(6)
  driver.find_element_by_xpath('//*[@id="proposalTab"]').click()
  sleep(2)
  driver.find_element_by_xpath('//*[@id="grantProposalEdit"]').click()
  sleep(3)
  if submitted_var == "No":
      driver.find_element_by_xpath('//*[@id="dueDate"]').send_keys(due_date)
      sleep(1)
  if match == "Match is required.":
      select = Select(driver.find_element_by_id('match'))
      select.select_by_visible_text("Yes")
      sleep(1)
  if match == "Match is not required.":
      select = Select(driver.find_element_by_id('match'))
      select.select_by_visible_text("No")
      sleep(1)
  driver.find_element_by_xpath('//*[@id="durationInMonths"]').send_keys(months)
  sleep(1)
  if submitted_var == "Yes":
      driver.find_element_by_xpath('//*[@id="submissionDate"]').send_keys(due_date)
      sleep(1)
  driver.find_element_by_xpath('//*[@id="budgetCeiling"]').send_keys(ceiling)
  sleep(1)
  driver.find_element_by_xpath('//*[@id="estimatedStartDate"]').send_keys(start_date)
  sleep(1)
  driver.find_element_by_xpath('//*[@id="grantProposalUpdateSave"]').click()
  sleep(2)
  driver.find_element_by_xpath('//*[@id="programTab"]').click()
  sleep(2)
  driver.find_element_by_xpath('//*[@id="grantProgramEdit"]').click()
  sleep(2)

  if role == "Prime":
      select = Select(driver.find_element_by_id('leadUnit'))
      select.select_by_visible_text("Prime")
      sleep(2)
  if role == "Solo":
      select = Select(driver.find_element_by_id('leadUnit'))
      select.select_by_visible_text("Solo")
      sleep(2)
  if role == "Sub":
      select = Select(driver.find_element_by_id('leadUnit'))
      select.select_by_visible_text("Sub")
      sleep(2)

  if opp_type == 'Development':
      select = Select(driver.find_element_by_id('CFCT_OR_ER'))
      select.select_by_visible_text("Child Focused Community Transformation")
      sleep(1)
  if opp_type == 'Relief':
      select = Select(driver.find_element_by_id('CFCT_OR_ER'))
      select.select_by_visible_text("Emergency Response")
      sleep(1)
      driver.find_element_by_xpath('//*[@id="sector-7"]').click()
      sleep(1)

  for i in sect_list:
      if i == "Education":
          driver.find_element_by_xpath('//*[@id="sector-1"]').click()
          sleep(1)
      if i == "FSL":
          driver.find_element_by_xpath('//*[@id="sector-2"]').click()
          sleep(1)
      if i == "Health":
          driver.find_element_by_xpath('//*[@id="sector-4"]').click()
          sleep(1)
      if i == "WASH":
          driver.find_element_by_xpath('//*[@id="sector-9"]').click()
          sleep(1)

      if i == "Gender":
          driver.find_element_by_xpath('//*[@id="sector-3"]').click()
          sleep(1)
      elif i == "Safeguarding":
          driver.find_element_by_xpath('//*[@id="sector-3"]').click()
          sleep(1)

  driver.find_element_by_xpath('//*[@id="grantProgramUpdateSave"]').click()
  sleep(3)

  return [google_file_string,wl3_entry_string]