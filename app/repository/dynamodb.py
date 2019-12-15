from app.repository.models import JobOffer


def save(payloads):
    JobOffer.create_table(read_capacity_units=1, write_capacity_units=1)

    for payload in payloads:
        job_offer = JobOffer()
        job_offer.hash = payload['hash']
        job_offer.url = payload['url']
        job_offer.position = payload['position']
        job_offer.description = payload['description']
        job_offer.company = payload['company']
        job_offer.date = payload['date']
        job_offer.tags = payload['tags']

        try:
            JobOffer.get(job_offer.hash)
        except JobOffer.DoesNotExist:
            job_offer.save()
