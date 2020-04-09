#!/usr/bin/env python
# coding: utf-8

# In[28]:


from qiskit import *


# In[29]:


qr = QuantumRegister(2)


# In[30]:


cr = ClassicalRegister(2)


# In[31]:


circuit = QuantumCircuit(qr, cr)


# In[32]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[33]:


circuit.draw()


# In[34]:


circuit.h(qr[0])


# In[35]:


circuit.draw(output='mpl')


# In[36]:


circuit.cx(qr[0], qr[1])


# In[37]:


circuit.draw(output='mpl')


# In[38]:


circuit.measure(qr, cr)


# In[39]:


circuit.draw(output='mpl')


# In[40]:


simulator = Aer.get_backend('qasm_simulator')


# In[41]:


result = execute(circuit, backend=simulator).result()


# In[42]:


from qiskit.tools.visualization import plot_histogram


# In[43]:


plot_histogram(result.get_counts(circuit))


# In[44]:


IBMQ.load_account()


# In[45]:


provider = IBMQ.get_provider('ibm-q')


# In[46]:


qcomp = provider.get_backend('ibmq_16_melbourne')


# In[47]:


job = execute(circuit, backend=qcomp)


# In[48]:


from qiskit.tools.monitor import job_monitor 


# In[49]:


job_monitor(job)


# In[50]:


result = job.result()


# In[51]:


plot_histogram(result.get_counts(circuit))


# In[ ]:




