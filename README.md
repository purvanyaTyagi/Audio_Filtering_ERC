
# Audio_Filtering_ERC

We are given A Amplitude-Modulated wav file. This file is noisy and the real frequencies are hidden.
To remove the Noise we follow these steps:
1) Identify the Carrier frequency which was used to Modulate the Signal
   We know that Freq modulation is basically encapsulated by the formula, ![image](https://github.com/user-attachments/assets/9d0724b4-04cd-4487-9389-b675f9099366)
   So, this basically means that our modulated signal is composed of a single frequency with varying amplitude

   Time Domain Graph of the Modulated Signal:
   ![image](https://github.com/user-attachments/assets/4a0c5434-3135-4754-9990-ab54bde2f95a)

   We Perform a FFT on this modulated signal to Identify the frequency with the highest energy. And that will be our carrier frequency

   This is the frequency Domain Graph of the Modulated signal created through np.FFT
   ![image](https://github.com/user-attachments/assets/43f5b4c6-a4fd-49c6-ba25-f27c6e9a3389)

   Here we can clearly find the peaks and Get our carrier frequency which came to be around 10582.31 hz.

   Now, with the Carrier frequency we can perform a Amplitude demodulation to get the orginal waveform.

   We can do this by multiplying our Original modulated signal with a sin wave of frequency = carrier frequency

   This is how the time domain graph of the demodulated signal looks like:
   ![image](https://github.com/user-attachments/assets/1e661e3e-f00a-407c-9775-b12df7c03623)


   Now that we have our demodulated original signal:

   We can perform a FFT On it to get its frqeuency domain waveform
   ![image](https://github.com/user-attachments/assets/34ef6d1d-8710-4720-ac31-aacf377c4680)

   Here we can clearly see, that there are a few peaks around the origin and at frequencies around 20khz.
   and apart from that there is a lot of noisy unwanted frequencies between them.

   To remove these unwanted noise we can use a bandpass filter.
   a bandpass filter can remove all the frequencies except the range given.
   for example bandpassfilter(1000, 1200) would only keep frequencies between 1000 to 1200 hz and remove all other frequencies in the wave form.

   We apply this to get this frequency domain- wave form

   ![image](https://github.com/user-attachments/assets/0946b7aa-8513-4140-8674-2aed08854472)

   A lot of noise is now removed.
   I also used a Shift frequency function that was able to shift all the frequencies in the waveform by -500.
   this reduced the high pitch of the sound i was getting.

   ![image](https://github.com/user-attachments/assets/5632aadb-42f1-4e1b-9198-036ecbfd252f)
   This is the function i used to perform the frequency shift.

   All the graphs were plotted through matplotlib.pyplot. The main.py has all the implementations and plotting code.

   Clean_output_real_real.wav is the final output :) 

   Final audio: (Andrew Garfield Laughing lol)

https://github.com/user-attachments/assets/9680e102-affc-4b56-863a-ee5f10bc511b

This audio still contains a lot of missing frequencies and noise issues, i couldnt get it to sound perfect. I will look into it more and hopefully get a cleaner version.




   



