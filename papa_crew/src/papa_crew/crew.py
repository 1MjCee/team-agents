from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from papa_crew.tools.custom_tool import TelegramBotTool
import os
from crewai import LLM

llm = LLM(
    model="ollama/llama3.1:8b",
    base_url="http://localhost:11434"
)

@CrewBase
class PapaCrew():
	"""TeamCrew crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# Defining Crew agents
	@agent
	def sales_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['sales_agent'],
			tools=[TelegramBotTool("7789761548:AAEncGEjI1kfCWg8GXcp7ZinCA1-GiyHKAk", -4712845613)],
			verbose=True,
			max_rpm=3,
			memory=True,
			llm=llm
		
		)

	@agent
	def marketing_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['marketing_agent'],
			tools=[TelegramBotTool("7789761548:AAEncGEjI1kfCWg8GXcp7ZinCA1-GiyHKAk", -4712845613)],
			verbose=True,
			max_rpm=3,
			memory=True,
			llm=llm
			
		)
	
	@agent
	def customer_service_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['customer_service_agent'],
			tools=[TelegramBotTool("7789761548:AAEncGEjI1kfCWg8GXcp7ZinCA1-GiyHKAk", -4712845613)],
			verbose=True,
			max_rpm=3,
			memory=True,
			llm=llm
			
		)

	# Defining Crew tasks
	@task
	def sales_highlights_task(self) -> Task:
		return Task(
			config=self.tasks_config['sales_highlights_task'],
		)

	@task
	def marketing_engagement_task(self) -> Task:
		return Task(
			config=self.tasks_config['marketing_engagement_task'],
		)
	
	@task
	def customer_support_task(self) -> Task:
		return Task(
			config=self.tasks_config['customer_support_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the TeamCrew crew"""
		

		return Crew(
			agents=self.agents,
			tasks=self.tasks, 
			process=Process.sequential,
			verbose=True,
			memory=True,
		)
